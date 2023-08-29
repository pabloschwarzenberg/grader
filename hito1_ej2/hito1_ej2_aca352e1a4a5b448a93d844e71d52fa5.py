#Algoritmo que evalua llamadas telefonicas.

#Solita numero telefonico.
numero_telefono = int(input("Ingrese numero de telefono : "))

control = True

#Validamos el telefono.
while control:
    if len(str(numero_telefono)) == 8:
        control = False
    else:
        numero_telefono = int(input("Numero debe contener 8 digitos, Ingrese numero de telefono nuevamente : "))
    
#Validamos la hora.
#Solita hora de llamda.
hora_llamada = int(input("Ingrese hora de llamada : "))
while hora_llamada <0 or hora_llamada > 23:
      hora_llamada = int(input("Hora de llamada incorrecta, Ingrese hora nuevamente : "))
    

#Evaluar cuando contestar e imprime respuesta.
if hora_llamada >= 0 and hora_llamada < 7:
    print("CONTESTAR")
elif hora_llamada < 14 and str(numero_telefono)[5 : 9] == "909":
    print("CONTESTAR")
elif hora_llamada > 17 and hora_llamada < 19 and str(numero_telefono)[0 : 3] != "877":    
    print("CONTESTAR")
else:
    print("NO CONTESTAR")