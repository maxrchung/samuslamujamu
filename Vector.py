import math

class Vector:
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    def normalize(self):
        dist = float(self.length())
        x = self.x / dist
        y = self.y / dist
        normalized = Vector([x, y])
        return normalized

    def length(self):
        dist = math.sqrt(self.x * self.x + self.y * self.y)
        return dist

    def lengthSquared(self):
        dist = self.x * self.x + self.y * self.y
        return dist

    def add(self, other):
        added = Vector([self.x + other.x, self.y + other.y])
        return added
    
    def minus(self, other):
        difference = Vector([self.x - other.x, self.y - other.y])
        return difference
    
    def multiply(self, value):
        multiplied = Vector([self.x * value, self.y * value])
        return multiplied
    
    def list(self):
        point = [self.x, self.y]
        return point

    def toString(self):
        print self.x, self.y
