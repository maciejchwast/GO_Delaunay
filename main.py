import random
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image, ImageDraw


class Point:
    def __init__(self, px, py):
        self.x = px
        self.y = py

    def print(self):
        return "X = " + str(round(self.x, 2)) + ", Y = " + str(round(self.y, 2))

    def toInt(self):
        self.x = int(self.x)
        self.y = int(self.y)

    def half(self):
        return Point(self.x/2, self.y/2)

    def invX(self):
        return Point(-self.x, self.y)

    def invY(self):
        return Point(self.x, -self.y)


class Straight:
    def print(self):
        return "y = " + str(round(self.a, 2)) + "X + " + str(round(self.b, 2))

    def __init__(self, p1: Point, p2: Point):
        self.a = (p1.y - p2.y) / (p1.x - p2.x)
        self.b = p1.y - self.a * p1.x


class Line:
    head: Point
    tail: Point

    def print(self):
        return "head point: " + self.head.print() + " tail point: " + self.tail.print()

    def __init__(self, p1: Point, p2: Point):
        self.head = p1
        self.tail = p2
        self.belongs_to_straight = Straight(p1, p2)


class Plot:
    plot = plt

    def __init__(self):
        self.plot.xlim(-1000, 1000)
        self.plot.ylim(-1000, 1000)


class PointCloud:
    points = []

    def __init__(self, center: Point, spread):
        self.points.clear()
        self.centerPoint = center
        self.spread = spread
        for i in range(random.randrange(10, 30)):
            newPoint = randomPointWithinDistance(self.spread, self.centerPoint)
            self.points.append(newPoint)
        self.pointCount = len(self.points)

    def draw(self, _color):
        for pt in self.points:
            plt.plot(pt.x, pt.y, '.', color=_color)
        plt.show()



    def printPoints(self):
        for pt in self.points:
            print("Point ", pt.x, ", ", pt.y)


class Circle:
    def __init__(self, center: Point, radius):
        self.center = center
        self.radius = radius


def randomPoint():
    a = random.randrange(-1000, 1000)
    b = random.randrange(-1000, 1000)
    return Point(a, b)


def pointDistance(p1: Point, p2: Point):
    return math.sqrt((p2.x * p2.x - p1.x * p1.x) - (p2.y * p2.y - p1.y * p1.y))


def randomPointExcludeArea(p1: Point, range):
    result = randomPoint()
    while pointDistance(result, p1) < range:
        result = randomPoint()
    return result


def randomPointWithinDistance(dist, p1: Point):
    result = Point(random.randrange(p1.x - dist, p1.x + dist), random.randrange(p1.y - dist, p1.y + dist))
    return result


def isInCircle(c, p: Point):
    result = False
    if(pointDistance(p,c.center)<c.radius):
        result = True
    return result


def circleOnTriangle(p1: Point, p2: Point, p3: Point):
    x12 = p1.x - p2.x
    x13 = p1.x - p3.x

    y12 = p1.y - p2.y
    y13 = p1.y - p3.y

    y31 = p3.y - p1.y
    y21 = p2.y - p1.y

    x31 = p3.x - p3.x
    x21 = p2.x - p1.x

    sx13 = pow(p1.x, 2) - pow(p3.x, 2)
    sy13 = pow(p1.y, 2) - pow(p3.y, 2)
    sx21 = pow(p2.x, 2) - pow(p1.x, 2)
    sy21 = pow(p2.y, 2) - pow(p1.y, 2)

    f = (sx13*x12 + sy13*x12 + sx21*x13 + sy21*x13)/(2 * (y31*x12 - y21*x13))
    g = (sx13*y12 + sy13*y12 + sx21*y13 + sy21*y13)/(2 * (x31*y12 - x21*y13))
    c = -pow(p1.x, 2) - pow(p1.y, 2) - 2*g*p1.x - 2*f*p1.y

    h = -g
    k = -f
    sqrt_of_r = pow(h, 2) + pow(k, 2) - c

    r = np.sqrt(sqrt_of_r)

    return Circle(Point(h, k), r)


if __name__ == '__main__':
    pointcloud = PointCloud(Point(0, 0), 1000)
    pointcloud.draw('red')


