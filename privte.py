
class A:
    def do_something(self):
        print("A")

class B(A):
    def do_something(self):
        print("B")
        super().do_something()

class C(A):
    def do_something(self):
        print("C")
        super().do_something()

class D(B, C):
    def do_something(self):
        print("D")
        super().do_something()

d = D()
d.do_something()


