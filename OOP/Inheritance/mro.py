class A:
	def do_something(self):
		print("Method from class: A")

class B(A):
	def do_something(self):
		print("Method from class: B")

class C(A):
	def do_something(self):
		print("Method from class: C")

class D(B,C):
	def do_something(self):
		print("Method from class: D")
		super().do_something()

test = D()
test.do_something()
# print(D.__mro__)
# print(D.mro())
# help(D)