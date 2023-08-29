#Descomponer un número
Numeros = str(input("Ingrese un numero de hasta 4 digitos: "))

if (int(Numeros) < 99):
    print(Numeros[0],"D + " + Numeros[1],"U")
elif (int(Numeros) < 999):
    print(Numeros[0],"C + " + Numeros[1],"D + " + Numeros[2],"U")
elif (int(Numeros) < 9999):
    print(Numeros[0],"M + " + Numeros[1],"C + " + Numeros[2],"D + " + Numeros[3],"U")    