#Contestador automático
#Le digo al usuario que ingrese un número de teléfono
n=(input("Ingrese un número telefónico:"))
#Le digo al usuario que ingrese la hora de la llamada
hora_llamada =int(input("Ingrese la hora de llamada:"))

if  (hora_llamada >= 0 and hora_llamada <=7): 
    print("CONTESTAR")
elif hora_llamada >= 8 and hora_llamada <=14 and int(n[5:8]) == 909:
    print("CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <=19 and int(n[5:8]) == 877:
    print("CONTESTAR")
else: 
    print("NO CONTESTAR")


