#Descomponer un número
x = int(input(" porfavor ingrese un número de un maximo de 4 digitos:"))
while len(str(x)) > 4 or x < 1:
    x = int(input("porfavor ingrese un número de un maximo de 4 digitos:"))
n = str(x)
if len(str(x)) == 1:
    print(n[0] + "U")
elif len(str(x)) == 2:
    print(n[0] + "D + " + n[1] + "U")
elif len(str(x)) == 3:
    print(n[0] + "C + " + n[1] + "D + " + n[2] + "U")
elif len(str(x)) == 4:
    print(n[0] + "M + " + n[1] + "C + " + n[2] + "D + " + n[3] + "U")