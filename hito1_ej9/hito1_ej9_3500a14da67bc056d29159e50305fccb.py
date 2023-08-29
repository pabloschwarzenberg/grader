X = int(input("Ingrese 1X: "))
Y = int(input("Ingrese 1Y: "))
P = int(input("Ingrese el primer resultado: "))

SX = int(input("Ingrese 2X: "))
SY = int(input("Ingrese 2Y: "))
S = int(input("Ingrese el segundo resultado: "))

T = (X * SY) - (SX * Y)
Tx = (P * SY) - (S * Y)
Ty = (X * S) - (SX * P)

X = Tx/T
Y = Ty/T

print("X=",X)
print("Y=",Y)