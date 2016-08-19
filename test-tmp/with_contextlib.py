# -*- coding: utf-8 -*-
from contextlib import contextmanager
@contextmanager
def demo():
    print '[Allocate resources]'
    print 'Code before yield-statement executes in __enter__'
    yield '***contextmanager demo***'
    print 'Code after yield-statement executes in __exit__'
with demo() as value:
    print 'Assigned Value:%s'%value