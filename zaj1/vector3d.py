import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
    
    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)   

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)
    
    @staticmethod
    def are_orthogonal(vector1, vector2):
        return vector1.dot(vector2) == 0

# Utworzenie obiektu klasy Vector3D
vec = Vector3D(5, 3, 2)
print(vec.x)

# Drukowanie obiektu
print(vec)
print(vec.norm())
print(vec + Vector3D(1,1,1))
print(vec - Vector3D(1,1,1))
print(vec * 3)
print(vec.dot(Vector3D(3,2,1)))
