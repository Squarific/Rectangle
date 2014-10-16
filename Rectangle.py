from Point import *
from Math import *

class Rectangle:
	def __init__ (self, point1, point2, angle=0):
		""" Implementation of a rectangle using two points rotated around the first point"""
		self.point1 = Point(point1.x, point1.y)
		self.point2 = Point(point2.x, point2.y)
		self.angle = angle

	def width (self):
		return abs(self.point1.x - self.point2.x)

	def height (self):
		return abs(self.point1.y - self.point2.y)

	def area (self):
		return self.width() * self.height()

	def move (self, dx, dy):
		self.p1.move(dx, dy)
		self.p2.move(dx, dy)

	def get_real_point2 ():
		""" Rotate point2 around point1"""
		return self.point2.rotate_around(self.point1, self.angle)

class Point (Point):
	def rotate_around (self, point, angle):
		""" Return a point rotated around a point with a given angle"""

		# Create a new point to do our calculations on
		realpoint2 = Point(self.x, self.y)

		# Calculate the cosine and sine to be used in the rotation matrix
		cosangle = cos(angle)
		sinangle = sin(angle)

		# Translate so that point is the new origin
		realpoint2.x -= point.x
		realpoint2.y -= point1.y

		# Multiply by the rotation matrix of the angle
		realpoint2.x = realpoint2.x * cosangle - realpoint2.y * sinangle
		realpoint2.y = realpoint2.x * sinangle + realpoint2.y * cosangle

		return realpoint2