#Contestador de celular
celu = str(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))
no = "NO CONTESTAR"
si = "CONTESTAR"
madrugada = 23<=19
final = celu[5:8]
comienzo = celu[0:3]
if hora <= 7 and hora >= 0:
    print(si)
elif hora <=14 and hora>=8 and final== "909":
    print(si)
elif hora >= 8 and hora <= 14:
    print(no)
elif hora <= 19 and hora >= 17 and comienzo == "877":
    print(no)
elif hora <= 19 and hora >= 17:
    print(si)
elif hora <= 23 and hora > 19:
    print(no)
