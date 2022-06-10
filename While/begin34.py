import random
X,Y = sorted([random.randrange(1,10) for i in range(2)])
A = random.randrange(3000,10000)
B = random.randrange(1000,3000)
price_X = A/X
price_Y = B/Y
print(X,"kg of chocolates = ",A," rubles")
print(Y,"kg of toffees = ",B," rubles")
print("1 kg of chocolates = {0:.2f} rubles".format(price_X))
print("1 kg of toffees = {0:.2f} rubles".format(price_Y))
print("Chocolate candy is more expensive \
than toffee, times:",round(price_X/price_Y))
									