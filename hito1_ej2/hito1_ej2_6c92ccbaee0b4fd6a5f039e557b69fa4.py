#Contestador de celular
Numero = str(input("Ingrese numero telefonico: "))
Hora = int(input("Ingrese hora de la llamada: "))
N1 = int(Numero[5:8])
N2 = int(Numero[0:3])
if Hora >= 0 and Hora <= 7:
    print("Resultado: CONTESTAR")
elif Hora <= 14 and N1 == 909:
    print("Resultado: CONTESTAR")
elif Hora >= 17 and Hora <= 19 and N2 != 877:
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")