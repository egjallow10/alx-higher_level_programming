#!/usr/bin/python3
""" Module `student` provides the `Student` class """


class Student:
    """ Represents a student"""
    def __init__(self, first_name, last_name, age):
        """
        Initializes the public instance attributes:
        `first_name`, `last_name`, and `age`.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns a dictionary representation of a `Student` instance """
        return self.__dict__


if __name__ == '__main__':
    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))
