A = int(input("Ingrese un número de hasta 4 digitos:"))
while len(str(A)) > 4 or A < 1:
 A = int(input("Ingrese un número de hasta 4 digitos:"))
num = str(A)
if len(str(A)) == 1:
    print(num[0] + "U")
elif len(str(A)) == 2:
    print(num[0] + "D + " + num[1] + "U")
elif len(str(A)) == 3:
    print(num[0] + "C + " + num[1] + "D + " + num[2] + "U")
elif len(str(A)) == 4:
    print(num[0] + "M + " + num[1] + "C + " + num[2] + "D + " + num[3] + "U")