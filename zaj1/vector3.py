class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}, Z: {self.z}"

    def pokaz_informacje(self):
        print(f"X: {self.x}, Y: {self.y}, Z: {self.z}")


# Utworzenie obiektu klasy Vector3
vec3 = Vector3(5, 3, 2)

# Drukowanie obiektu
print(vec3)
vec3.pokaz_informacje()