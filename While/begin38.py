import random
r = list(range(-10,0)) + list(range(1,11))
A = random.choice(r)
B = random.randrange(-20,21)
x = -B/A
y = A * x + B
print("Ax + B = 0")
print("A = ",A)
print("B = ",B)
print("x = ",-B/A)
print("({0}) * ({1}) + ({2}) = {3}".format(A,x,B,y))
 
									