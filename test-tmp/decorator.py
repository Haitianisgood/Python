# -*- coding: utf-8 -*-
def f1(arg):
    print 'f1'
    r1 = arg()
    print r1
    return r1 + '+f1'
@f1
def f2(arg = ""):
    print 'f2'
    return arg +'+f2re'
print 'start'
print f2
# print f2('1')
#print f1(None)