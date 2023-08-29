#Descomponer un número
x = int(input(" porfavor ingrese un número de un maximo de 4 digitos:"))
while len(str(x)) > 4 or x < 1:
    x = int(input("porfavor ingrese un número de un maximo de 4 digitos:"))
y = str(x)
if len(str(x)) == 1:
    print(y[0] + "U")
elif len(str(x)) == 2:
    print(y[0] + "D + " + y[1] + "U")
elif len(str(x)) == 3:
    print(y[0] + "C + " + y[1] + "D + " + y[2] + "U")
elif len(str(x)) == 4:
    print(y[0] + "M + " + y[1] + "C + " + y[2] + "D + " + y[3] + "U")