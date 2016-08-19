# -*- coding: utf-8 -*-
import threading
import time

class Mythread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id=id
    
    def run(self):
        x=0
        time.sleep(60)
        print self.id
    
    def func(self):
        t.start()
        for i in range(5):
            print i
class test1():
    """docstring for test1"""
    def ab(self):
       print "aaa"

    
        
# t=Mythread(2)
# # t.func()
# b= test1()
# b.ab()
