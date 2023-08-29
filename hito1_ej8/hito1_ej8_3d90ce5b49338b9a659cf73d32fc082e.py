#Descomponer un número
#Fue entretenido sin ciclos
numero = int(input("Ingrese un numero (Maximo 4 cifras)"))
descomposicion = ""
if numero // 1000 != 0:
    descomposicion = str(numero // 1000) + "M + "
    numero = numero % 1000
    descomposicion+= str(numero // 100 ) + "C + "
    numero = numero % 100
    descomposicion += str(numero // 10) + "D + "
    numero = numero % 10
    descomposicion += str(numero) + "U"
    print(descomposicion)
elif numero // 100 != 0:
    descomposicion+= str(numero // 100 ) + "C + "
    numero = numero % 100
    descomposicion += str(numero // 10) + "D + "
    numero = numero % 10
    descomposicion += str(numero) + "U"
    print(descomposicion)
elif numero // 10 != 0:
    descomposicion += str(numero // 10) + "D + "
    numero = numero % 10
    descomposicion += str(numero) + "U"
    print(descomposicion)
else:
    print(str(numero)+ "U")