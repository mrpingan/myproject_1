# coding:utf-8
__author__ = "ping"
__date__ = "2018/12/1 22:37"

import hashids

def hashid(_id,length=6):
    KEY = "ping"
    hasher = hashids.Hashids(salt=KEY,min_length=length)
    return hasher.encode(_id)
