num = str(int(input("ingrese  numero de telefono:")))
llamada= int(input("ingrese hora de llamada:"))
extraer_subcadena = num[5:8]
extraer_subcadena2 = num[0:3]
x = str("909")
j = str("877")

if llamada >= 0 and llamada <=7:
    print("contestar")

if llamada>7 and llamada<=14 and extraer_subcadena==x:
    print("contestar")
else:
    print("no contestar")

if llamada>=17 and llamada<=19:
    if extraer_subcadena2 == j:
        print("no contestas")
    else:
        print("contestas")

if llamada>19:
    print("no contestas")