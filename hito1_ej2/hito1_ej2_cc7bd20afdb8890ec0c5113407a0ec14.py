NT=int(input("Ingresa tu número telefónico:"))
while (NT>99999999 or NT<9999999):
    NT=int(input("El número tiene que ser de 8 dígitos."))
    
    
H=int(input("Ingresa la hora de la llamada:"))
while (H<0 or H>=24):
    H=int(input("La hora tiene que estar entre las 0 y 24 horas."))
NTE=NT%1000
    
if (H<=7 and H>=0):
    print("Contestar")
elif (H>7 and H<14 and NTE==909):
    print("Contestar")
elif (H>7 and H<14):
    print("No Contestar")
elif (17<=H and H<=19 and NTE==877):
    print("No Contestar")
elif (17<=H and H<=19):
    print("No Contestar")   
elif (H>19):
    print("No contestar")
else:
    print("Contestar")
