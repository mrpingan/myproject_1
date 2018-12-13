FROM python:3.5.2

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["yum","install","uwsgi uwsgi-devel uwsgi-plugin-python"]

CMD ["/bin/sh","start_server.sh"]

CMD ["tail","start_server.sh"]


