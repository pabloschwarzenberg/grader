#Descomponer un número
#pedir numero
N = int(input("Ingrese un numero de maximo 4 digitos:"))
#proceso y salidas
while len(str(N)) > 4 or N < 1:
    N = int(input("Ingrese un numero de maximo 4 digitos:"))
DN = str(N)
if len(str(N)) == 1:
    print(DN[0] + "U")
elif len(str(N)) == 2:
    print(DN[0] + "D + " + DN[1] + "U")
elif len(str(N)) == 3:
    print(DN[0] + "C + " + DN[1] + "D + " + DN[2] + "U")
elif len(str(N)) == 4:
    print(DN[0] + "M + "+ DN[1] + "C +"+ DN[2] + "D +"+ DN[3]+"U")