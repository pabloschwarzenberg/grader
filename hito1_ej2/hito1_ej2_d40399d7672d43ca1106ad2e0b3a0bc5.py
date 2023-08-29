#Contestador de celular
#Entradas
número = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))

#Procesos
if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora >= 7 and hora <= 14 and ((número % 1000) == 909):
    print("CONTESTAR")
elif hora >= 17 and hora <= 19 and ((número // 100000) == 877):
    print("NO CONTESTAR")
elif hora >= 17 and hora <= 19:
     print("CONTESTAR")
else: print("NO CONTESTAR")      