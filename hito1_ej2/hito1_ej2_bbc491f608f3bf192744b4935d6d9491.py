#Contestador de celular
numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))

if hora >= 0 and hora < 7:
    print("CONTESTAR")
elif hora < 14 and numero % 1000 == 909:
    print("CONTESTAR")
elif hora >= 17 and hora < 19 and str(numero)[0:3] != '877':
    print("CONTESTAR")
else:
    print("NO CONTESTAR")