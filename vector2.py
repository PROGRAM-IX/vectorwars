import math

class Vector2():
    """Most of this taken from Will McGugan's Beginning Game Development 
    with Python and Pygame"""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)
    
    @staticmethod
    def from_points(a, b):
        return Vector2(b[0]-a[0], b[1]-a[1])

    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalised(self):
        magnitude = self.get_magnitude()
        if not magnitude == 0:
            return Vector2(self.x * 1/magnitude, self.y * 1/magnitude)
        else:
            return Vector2(self.x, self.y)
    
    # my dot product function
    def dot_product(self, other):
        # A dot B = A B cos theta = |A||B| cos theta
        # or A dot B = AxBx + AyBy + AzBz
        return self.x*other.x + self.y*other.y
    
    def cross_product(self, other):
        return self.x * other.y - self.y * other.x 
    
    @staticmethod
    def clamp(x, a, b):
        return min(max(x, a), b)

    def radians_between(self, other):
        own = Vector2(self.x, self.y)
        v = Vector2(other.x, other.y)
        own.normalise()
        v.normalise()
        #d_p = (self.clamp(self.dot_product(other), -1.0, 1.0))
        d_p = (self.dot_product(other))
        mag_self = own.get_magnitude()
        mag_other = v.get_magnitude()
        cos_of_angle = d_p/(mag_self*mag_other)
        return math.acos(cos_of_angle)

    
    def __add__(self, rhs): # rhs = right hand side of + operation
        return Vector2(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)

    def __neg__(self, rhs):
        return Vector2(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

