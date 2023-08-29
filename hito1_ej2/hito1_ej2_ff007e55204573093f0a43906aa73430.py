#Contestador de celular
 
numero = int(input("Ingrese numero telefonico(solo 8 cifras): "))
hora = int(input("Ingrese hora de la llamada(0 a 23): "))


if hora >= 0 and hora <= 7:
    print("Contestar")
elif numero % 1000 == 909:
         print("Contestar")
elif hora >= 17 and hora <= 19 and numero // 100000 != 877:
    print("Contestar")
elif hora > 19:
    print("No Contestar")
else:
    print("No Contestar")