#Contestador de celular
n= str(int(input("ingrese numero telefonico: ")))
horallamada= int(input("ingrese horade llamada: "))
extraer_subcadena= n[5:8]
extraer_subcadena2= n[0:3]
x= str("909")
j= str("877")

if horallamada >= 0 and horallamada <=7:
    print("contestar")
    
if horallamada>7 and horallamada<=14 and extraer_subcadena==x:
    print("contestar")
else:
    print("no contestar")
    
if horallamada>=17 and horallamada<=19:
    if extraer_subcadena2 == j:
        print("no contestar")
    else:
        print("contestar")
        
if horallamada>19:
    print("no contestar")