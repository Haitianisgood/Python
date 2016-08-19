#-*- coding: utf-8 -*-
class myDecorator(object):
    """docstring for myDecorator"""
    def __init__(self, f):
        print "inside myDecorator.__init__()"
        self.f = f
    def __call__(self):
        print "inside myDecorator.__call__"
        self.f()

@myDecorator
def aFunction():
    print "inside aFunction()"

@myDecorator
def b():
    print "inside b"
print "Finished decorating aFunction()"

aFunction()
b()




