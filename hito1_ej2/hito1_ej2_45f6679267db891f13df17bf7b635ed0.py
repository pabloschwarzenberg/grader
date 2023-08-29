#Contestador de celular
num = str(int(input("ingrese  numero de telefono:")))
horallamada = int(input("ingrese hora de llamada:"))
extraer_subcadena = num[5:8]
extraer_subcadena2 = num[0:3]
x = str("909")
j = str("877")

if horallamada >= 0 and horallamada <=7:
    print("contestar")

if horallamada>7 and horallamada<=14 and extraer_subcadena==x:
    print("contestar")
else:
    print("no contestar")
    
if horallamada>=17 and horallamada<=19:
    if extraer_subcadena2 == j:
        print("no contestas")
    else:
        print("contestas")
        
if horallamada>19:
    print("no contestas")