#Descomponer un número
# Variables
a = int(input("Ingrese un numero de hasta 4 digitos: "))
while len(str(a)) > 4 or a < 1:
    a = int(input("Ingrese  un numero de hasta 4 digitos: "))
ma = str(a)
if len(str(a)) == 1:
    print(ma[0] + "U")
elif len(str(a)) == 2:
    print(ma[0] + "D + " + ma[1] + "U")
elif len(str(a)) == 3:
    print(ma[0] + "C + " + ma[1] + "D + " + ma[2] + "U")
elif len(str(a)) == 4:
    print(ma[0] + "M + " + ma[1] + "C + " + ma[2] + "D + " + ma[3] + "U")
