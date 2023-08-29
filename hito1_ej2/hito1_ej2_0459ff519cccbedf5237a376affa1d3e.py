#Contestador de celular
num = str(int(input("ingrese el numero de telefono:")))
hora_llamada = int(input("indique hora de llamada:"))
extraer_subcadena = num[5:8]
extraer_subcadena2 = num[0:3]
x = str("909")
j = str("877")

if hora_llamada >= 0 and hora_llamada <=7:
    print("debes contestar")

if hora_llamada>7 and hora_llamada<=14 and extraer_subcadena==x:
    print("debes contestar")
else:
    print("no contestar")
    
if hora_llamada>=17 and hora_llamada<=19:
    if extraer_subcadena2 == j:
        print("no contestar")
    else:
        print("debes contestar")
        
if hora_llamada>19:
    print("no contestar")