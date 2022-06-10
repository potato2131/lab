import random
a = random.randrange(1,10)
b = random.randrange(1,10)
c = random.randrange(1,10)
print("Прямоугольный параллелепипед")
print("Ребро a: ", a)
print("Ребро b: ", b)
print("Ребро c: ", c)
V = a*b*c
print("Объем: ", V)
S = 2*(a*b + b*c + a*c)
print("Площадь поверхности: ", S)
									