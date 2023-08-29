#Contestador de celular
import datetime

numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))

if hora >= 0 and hora < 7:
    print("CONTESTAR")
elif hora >= 7 and hora < 14:
    if numero % 100 == 9:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 17 and hora < 19:
    if numero // 1000000 == 877:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
else:
    print("NO CONTESTAR")