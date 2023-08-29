nt = int(input("Ingrese 8 números: "))
while not(nt>10000000 and nt<=99999999):
    nt = int(input("Error en el número telefonico, ingrese de nuevo el número: "))

hora = int(input("Ingrese una hora del día: "))
while not(hora>=0 and hora<23):
    hora=int(input("Error en la hora del día, ingrese de nuevo la hora: "))

tres_ultimos_numeros = nt%1000
tres_primeros_numeros = nt//100000

if hora>=0 and hora<=7:
    print("CONTESTAR")
elif hora<14 and tres_ultimos_numeros!=909:
    print("NO CONTESTAR")
elif hora<14 and tres_ultimos_numeros==909:
    print("CONTESTAR")

elif hora>=14 and hora<17:
    print("NO CONTESTAR")
elif hora>=17 and hora<19 and tres_primeros_numeros!=877:
    print("CONTESTAR")
elif hora>=17 and hora<19 and tres_primeros_numeros==877:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")