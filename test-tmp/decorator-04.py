#-*- coding: utf-8 -*-
def addspam(fn):
    def new(*args):
        print "spam****"
        return fn(*args)
    return new

@addspam
def  useful(a,b):
    print a**2+b**2

print "finish....decorating"
useful(4,3)