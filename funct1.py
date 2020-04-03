class A:

    def __init__(self):
        print("This is Class Constructor")

    def add(self, a, b):
        print(a + b)

    def sub(self, a, b):
        return a - b


o = A()
o.add(23, 11)
x = o.sub(11, 3)
print(x)
