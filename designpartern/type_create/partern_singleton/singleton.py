# coding=utf-8
__author__ = 'TIF'


class _Singleton(object):
    pass


Singleton = _Singleton()

del _Singleton

another = Singleton.__class__()

print (type(another))