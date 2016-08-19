# -*- coding: utf-8 -*-
class myfirstclass(object):
    """docstring for myfirstclass"""
    def __init__(self, nm='bb'):
        # super(myfirstclass, self).__init__()
        # self.arg = arg
        self.name = nm
        print 'nm name',nm
    def showname(self):
        print "Your name is ",self.name
        print 'My name is',self.__class__.__name__


# def times(x,y):
#     return(x*y)       
# print times(2,3)
# print times('ab',3)
f2 = myfirstclass('jj')
f2.showname()
