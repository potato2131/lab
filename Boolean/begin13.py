import random
import math
print("Пи:", math.pi)
R1 = random.randrange(2,10)
R2 = random.randrange(1,R1)
print("Радиус 1: ", R1)
print("Радиус 2: ", R2)
S1 = math.pi * R1**2
S2 = math.pi * R2**2
S3 = S1 - S2
print("Площадь круга 1: ", S1)
print("Площадь круга 2: ", S2)
print("Площадь кольца: ", S3)
									