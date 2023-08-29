#Descomponer un número
 numero=int(input("ingrese un numero de maximo 4 digitos"))
num = str(numero)

if(numero<10000 and numero>999):


    print(num[0],"M", num[1],"C", num[2],"D", num[3],"U")


if(numero<1000 and numero>99):

    print(num[0], "C", num[1],"D", num[2],"U")

if(numero<100 and numero>9):

    print(num[0], "D" ,num[1],"U")

if(numero<10 and numero>=0):

    print(num[0], "U")