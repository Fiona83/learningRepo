# This file is added to the repository for a part of the assignment from my Coursera course "Getting started with Git and GitHub"
# the code is also a part of my self learning of Python
# Test the abnormal written style of if statement

# Author: Fiona Chen
# Date: 2022-09-13

class Person(object):

  __slots__ = ('_name', '_age', '_gender')

  def __init__(self, name, age, gender):
    self._name = name
    self._age = age
    self._gender = gender

  @property
  def name(self):
    return self._name

  @property
  def age(self):
    return self._age

  @property
  def gender(self):
    return self._gender

  @age.setter
  def age(age):
    self._age = age
    return self._age


  def __str__(self):
    return "%s is %s years old." % (self._name, self._age)

age = input("Please input the age:")
fiona = Person("Fiona", age, "f")
print(fiona)
