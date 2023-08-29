#Descomponer un número
z = int(input("Ingrese un número de hasta 4 digitos:"))
while len(str(z)) > 4 or z < 1:
 z = int(input("Ingrese un número de hasta 4 digitos:"))
num = str(z)
if len(str(z)) == 1:
    print(num[0] + "U")
elif len(str(z)) == 2:
    print(num[0] + "D + " + num[1] + "U")
elif len(str(z)) == 3:
    print(num[0] + "C + " + num[1] + "D + " + num[2] + "U")
elif len(str(z)) == 4:
    print(num[0] + "M + " + num[1] + "C + " + num[2] + "D + " + num[3] + "U")      