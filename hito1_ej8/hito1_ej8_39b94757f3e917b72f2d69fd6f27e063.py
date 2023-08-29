#Descomponer un número
n = int(input("Ingrese un numero de solamente 4 digitos:"))
while len(str(n)) > 4 or n < 1:
    n = int(input("ingresar un numero de 4 digitos de lo contrario no funcionara:"))
num = str(n)
if len(str(n)) == 1:
    print(num[0] + "u")
elif len(str(n)) == 2:
    print(num[0] + "d + " + num[1] + "u")
elif len(str(n)) == 3:
    print(num[0] + "c + " + num[1] + "d + " + num[2] + "u")
elif len(str(n)) == 4:
    print(num[0] + "m + " + num[1] + "c + " + num[2] + "d + " + num[3] + "u")       