PraX = int(input("Ingrese 1X: "))
PraY = int(input("Ingrese 1Y: "))
PrRdo = int(input("Ingrese el primer resultado: "))

SdaX = int(input("Ingrese 2X: "))
SdaY = int(input("Ingrese 2Y: "))
SdRdo = int(input("Ingrese el segundo resultado: "))

T = (PraX * SdaY) - (SdaX * PraY)
Tx = (PrRdo * SdaY) - (SdRdo * PraY)
Ty = (PraX * SdRdo) - (SdaX * PrRdo)

X = Tx/T
Y = Ty/T

print("X=",X)
print("Y=",Y)