#Contestador de celular
numero_telefono = str(input("Ingrese el número telefónico "))
hora_llamada = int(input("Ingrese hora de la llamada "))
termina = int(numero_telefono[5:8])
comienza = int(numero_telefono[0:2])

if 0 < hora_llamada <=7:
    print ("CONTESTAR")
    
if hora_llamada <=14 and termina != 909:
    print ("NO CONTESTAR")

if hora_llamada <=14 and termina == 909:
    print ("CONTESTAR")

if 17 < hora_llamada <=19 and comienza != 877:
    print ("NO CONTESTAR")
  
if 17 < hora_llamada <=19 and comienza == 877:
    print ("CONTESTAR")
   
if hora_llamada >=19:
    print ("NO CONTESTAR")
