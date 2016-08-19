class A(object):
    """docstring for A"""
    def __init__(self, name):
        self.name = name
    def getName(self):
        return 'A'+self.name

class C(A):
    """docstring for C"""
    def __init__(self, name):
        super(C, self).__init__(name)
    def getName(self):
        return 'C '+self.name

if __name__=='__main__':
    c=C('Hello')
    print c.getName()
        
        