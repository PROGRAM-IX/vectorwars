import math

class vector2():
    """Most of this taken from Will McGugan's Beginning Game Development 
    with Python and Pygame"""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)
    
    @staticmethod
    def from_points(a, b):
        return vector2(b[0]-a[0], b[1]-a[1])

    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalise(self):
        magnitude = self.get_magnitude()
        self.x = magnitude/self.x
        self.y = magnitude/self.y
    
    # my dot product function
    def dot_product(self, other):
        # A dot B = A B cos theta = |A||B| cos theta
        # or A dot B = AxBx + AyBy + AzBz
        return self.x*other.x + self.y*other.y

    def angle_between(self, other):
        # cos(theta) = 1/(|A||B|)
        #d = (1/(self.get_magnitude()*other.get_magnitude()))
        #print d
        #return math.acosh(d)
        pass

    def __add__(self, rhs): # rhs = right hand side of + operation
        return vector2(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return vector2(self.x - rhs.x, self.y - rhs.y)

    def __neg__(self, rhs):
        return vector2(-self.x, -self.y)

    def __mul__(self, scalar):
        return vector2(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        return vector2(self.x / scalar, self.y / scalar)

