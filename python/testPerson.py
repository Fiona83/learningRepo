"""
This file is added to the repository for a part of the assignment
from my Coursera course "Getting started with Git and GitHub".
The code is also a part of my self learning of Python.

+ Test the abnormal written style of if statement

# Author: Fiona Chen
# Date: 2022-09-13
"""


class Person(object):

    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        if gender != "m" and gender != "f":
            print("Invalid gender for %s. (m/f)" % self._name)
            quit()
        self._gender = gender
        # debugging
        # print(type(self._name), type(self._age), type(self._gender))

    def __str__(self):
        #return "%s is " % self._name + "%d years old." % self._age
        strGender = "male" if self._gender == "m" else "female"
        return "Name: %s, Age: %d, Gender: %s" % \
        (self._name, self._age, strGender)

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
    def age(self, age):
        self._age = age
        return self._age



    def watch_tv(self):
        # try this compact coding style
        tv = "Netflix" if self._age >= 18 else "Youtube Kids"
        return tv
        """
        if self._age < 18:
            tv = "Youtube Kids"
        else:
            tv = "Netflix"
        return tv
        """

# main function
fiona = Person("Fiona", 35, "f")
print(fiona)

# update the age
age = input("Please update the age:")
fiona.age = int(age)
print(fiona)

ella = Person("Ella", 4, "f")
eddie = Person("Eddie", 1, "m")
print("%s is watching %s." % (ella.name, ella.watch_tv()))
print("%s is watching %s." % (fiona.name, fiona.watch_tv()))
print("%s is watching %s" % (eddie.name, eddie.watch_tv()))


# test gender control
#wang = Person("Lao Wang", 50, "k")
#print(wang)
