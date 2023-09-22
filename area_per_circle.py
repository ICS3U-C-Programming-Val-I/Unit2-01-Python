#!/usr/bin/env python3
# Created By: Val Ijaola
# Date: September 18, 2023
# This program Calculates the area and perimeter of a circle with a radius of 5.7cm.


import math

rad = 5.7


def main():
    print("If a circle has the radius of 5.7cm:")
    print("The circumference of the circle is {:.2f}cm.".format(math.pi * rad * 2))
    print("The area of the circle is {:.2f}cm.".format(math.pi * rad**2))


if __name__ == "__main__":
    main()
