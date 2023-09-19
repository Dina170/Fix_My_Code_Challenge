#!/usr/bin/python3
"""Defines a square class."""


class Square():
    """Represent a square."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize a new Square."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Gets the area of the Square."""
        return self.width * self.height

    def permiter_of_my_square(self):
        """Gets the perimeter of the Square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
