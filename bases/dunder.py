class Hola:
    def __init__(self):
        self.v = 5

    def __truediv__(self, num):
        self.v /= 5
        return self

h = Hola()
a = h/2
print(a)
print(a.v)