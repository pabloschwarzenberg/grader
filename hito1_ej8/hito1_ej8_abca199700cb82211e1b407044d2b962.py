#Descomponer un número
N = int(input("Ingrese un número de hasta cuatro dígitos:"))
while len(str(N)) > 4 or N < 1:
 N = int(input("Ingrese un número de hasta cuatro dígitos:"))
num = str(N)
if len(str(N)) == 1:
    print(num[0] + "U")
elif len(str(N)) == 2:
    print(num[0] + "D + " + num[1] + "U")
elif len(str(N)) == 3:
    print(num[0] + "C + " + num[1] + "D + " + num[2] + "U")
elif len(str(N)) == 4:
    print(num[0] + "M + " + num[1] + "C + " + num[2] + "D + " + num[3] + "U")