#Contestador de celular
num = str(int(input("ingrese el numero del telefono:")))
hora_de_llamada = int(input("ingrese la hora de llamada:"))
extraer_la_subcadena = num[5:8]
extraer_la_subcadena2 = num[0:3]
x = str("909")
j = str("877")

if hora_de_llamada >= 0 and hora_de_llamada <=7:
    print("contestar")

if hora_de_llamada>7 and hora_de_llamada<=14 and extraer_la_subcadena==x:
    print("contestar")
else:
    print("no contestar")

if hora_de_llamada>=17 and hora_de_llamada<=19:
    if extraer_la_subcadena2 == j:
        print("no contestar")
    else:
        print("contestar")

if hora_de_llamada>19:
    print("no contestar")