#Contestador de celular
numero = input('Ingrese número telefónico: ')
hora = int(input('Ingrese la hora de la llamada: '))

if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora < 14 and numero.endswith("909"):
    print("CONTESTAR")
elif hora >= 17 and hora <= 19 and numero.startswith("877"):
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
