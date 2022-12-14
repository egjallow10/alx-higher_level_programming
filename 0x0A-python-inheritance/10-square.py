#!/usr/bin/python3
""" Module `10-square` provides the `Square` class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a `Square` class that inherits from `Rectangle` """
    def __init__(self, size):
        """ Initializes validated private `__width` """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """" returns the area of the square """
        return self.__size ** 2


if __name__ == '__main__':
    s = Square(13)

    print(s)
    print(s.area())