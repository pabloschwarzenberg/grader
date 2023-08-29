#Contestador de celular
num_de_tel = str(int(input("ingrese  numero de telefono:")))
hora_de_la_llamada = int(input("ingrese hora de la llamada:"))
no_contestar = num_de_tel[5:8]
no_contestar_2 = num_de_tel[0:3]
x = str("909")
j = str("877")

if hora_de_la_llamada >= 0 and hora_de_la_llamada <=7:
    print("contestar")

if hora_de_la_llamada>7 and hora_de_la_llamada<=14 and no_contestar ==x:
    print("contestar")
else:
    print("no contestar")
    
if hora_de_la_llamada>=17 and hora_de_la_llamada<=19:
    if no_contestar_2 == j:
        print("no contestar")
    else:
        print("contestar")
        
if hora_de_la_llamada>19:
    print("no contestar")