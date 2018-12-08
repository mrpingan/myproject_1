from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseBadRequest
from django.urls import reverse
from django.conf import settings
from apps.account.form import LoginForm
from apps.account.models import GithubUser,MyUser

import uuid
import requests


def login_view(request):
    context = {}
    if request.method == "GET":
        context['form'] = LoginForm
        return render(request,"login.html",context)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    return HttpResponse('<h1>Login Failed</h1>')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def auth_github_view(request):
    url = 'https://github.com/login/oauth/authorize?scope=user:email' \
          '&client_id=%s&state=%s' % (settings.AUTH['github']['client_id'],uuid.uuid4().hex)
    print(url)
    return HttpResponseRedirect(url)

def auth_github_callback_view(request):

    code = request.GET.get('code',None)
    state = request.GET.get('state',None)

    if code is None or state is None:
        return HttpResponseBadRequest(reason="参数错误")


    token_url = 'https://github.com/login/oauth/access_token'
    data = {
        'client_id':settings.AUTH['github']['client_id'],
        'client_secret':settings.AUTH['github']['client_secret'],
        'code':code,
        'state':state
    }

    res = requests.post(token_url,data=data)
    # import pdb;pdb.set_trace()
    result = res.text.split('&')
    access_token = result[0].split('=')[1]
    # import pdb;pdb.set_trace()
    if access_token == "bad_verification_code":
        return HttpResponseBadRequest("获取token错误")

    user_url = "https://api.github.com/user?access_token=" + access_token

    req = requests.get(user_url)
    auth_result = req.json()
    dbUser = auth_to_db(auth_result)

    # 登录
    user = authenticate(username=dbUser.username,password=settings.SECRET_KEY)

    if user is not None:
        # import pdb;pdb.set_trace()
        login(request,user)
        return HttpResponseRedirect(reverse('index'))
    return HttpResponse('<h1>Login Failed</h1>')

def auth_to_db(result):
    gid = str(result['id'])
    slogin = str(result['login'])

    gitusers = GithubUser.objects.filter(gid=gid)
    if gitusers.exists():
        gituser = gitusers[0]
    else:
        gituser = GithubUser()
        gituser.gid = gid
        gitusers.login = slogin
        gituser.repos_url = result.get('repos_url', '')
        gituser.url = result.get('url', '')
        gituser.follower_url = result.get('follower_url', '')
        gituser.subscriptions_url = result.get('subscriptions_url', '')
        gituser.html_url = result.get('html_url', '')
        gituser.organizations_url = result.get('organizations_url', '')
        gituser.public_gists = result.get('public_gists', '')
        gituser.created_at = result.get('created_at', '')


    gituser.name = result.get('name','')
    gituser.email = result.get('email','')
    gituser.bio = result.get('bio','')
    gituser.location = result.get('location','')
    gituser.updated_at = result.get('updated_at','')
    gituser.avatar_url = result.get('avatar_url','')
    gituser.followers = int(result.get('followers',0))
    gituser.public_repos = int(result.get('public_repos',0))

    gituser.save() # 保存到数据库

    if gituser.user is None:
        user = MyUser()
        user.username = slogin
        user.email = gituser.email if gituser.email else "{}@github.com".format(slogin)
        user.set_password(settings.SECRET_KEY)
        user.avatar = gituser.avatar_url
        user.nickname = gituser.name
        user.save()

        # gituser 与 user 关联
        gituser.user = user
        gituser.save()

        return user

    else:
        gituser.user.avatar = gituser.avatar_url
        gituser.user.nickname = gituser.name
        gituser.user.save()

        return gituser.user
