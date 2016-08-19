#-*- coding: utf-8 -*-
class Person(object):
    """docstring for Person"""
    def __init__(self, first_name,lastname):        
        self.first_name = first_name
        self.lastname = lastname
    
    @property
    def full_name(self):
        """Return the full name"""
        return "%s %s" %(self.first_name,self.lastname)


person = Person("Mike","Driscoll")

print person.first_name
print person.full_name

person.first_name = "Dan"
print person.full_name