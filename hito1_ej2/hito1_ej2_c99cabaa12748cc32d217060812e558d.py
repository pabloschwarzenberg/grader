#Contestador de celular
Telefono=input("Ingrese numero telefonico: ")
Hora=int(input("Ingrese hora de la llamada: "))
PrimerosNumeros = str(Telefono)[0:3]
UltimosNumeros = str(Telefono)[5:8]

#CONDICIONAL
if Hora > 7 and Hora <= 14:
    if UltimosNumeros == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if Hora >= 17 and Hora <= 19:
    if PrimerosNumeros == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
# CONTESTA SIEMPRE
if Hora >= 0 and Hora <= 7:
    print("CONTESTAR")
# NO CONTESTA NUNCA
if (Hora >= 15 and Hora <= 16) or (Hora >= 20 and Hora <= 23):
    print("NO CONTESTAR")