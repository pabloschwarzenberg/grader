#Contestador de celular
#Contestador de celular
num_telefono = int(input("Ingrese un número telefónico de 8 cifras: "))
hora = int(input("Ingrese la hora de la llamada: "))

num_telefono = str(num_telefono)
num_909 = num_telefono[5:9]
num_877 = num_telefono[0:3]


#Condiciones
if 0 <= hora and hora <= 7:
    print("Resultado: CONTESTAR")
elif  hora > 7 and hora < 14:
    if num_909 == "909":
        print("Resultado: CONTESTAR")

    else:
        print("Resultado: NO CONTESTAR")
elif hora > 17 and hora < 19:
    if num_877 == "877":
        print("Resultado: NO CONTESTAR")

    else:print("Resultado: NO CONTESTAR")

else:
    print("Resultado: NO CONTESTAR")      