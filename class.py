# defining a class
# class Dog:
#  attr1 = "mamal"
#  attr2 = "dog"
#  def fun(self):print(" I 'm a", self.attr2)   
# abc= Dog()
# print(abc.attr2)     
# abc.fun() 

class Person:
  def _init_(self,name):
   self.name=name
  def say_hi(self):print('hello , my nmae is',self.name)
p = Person('james')
p.say_hi()
