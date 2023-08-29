#Descomponer un número
X = int(input("Introduzca un número de hasta 4 digitos:"))
while len(str(X)) > 4 or X < 1:
 X = int(input("Introduzca un número de hasta 4 digitos:"))
num = str(X)
if len(str(X)) == 1:
    print(num[0] + "U")
elif len(str(X)) == 2:
    print(num[0] + "D + " + num[1] + "U")
elif len(str(X)) == 3:
    print(num[0] + "C + " + num[1] + "D + " + num[2] + "U")
elif len(str(X)) == 4:
    print(num[0] + "M + " + num[1] + "C + " + num[2] + "D + " + num[3] + "U")
      