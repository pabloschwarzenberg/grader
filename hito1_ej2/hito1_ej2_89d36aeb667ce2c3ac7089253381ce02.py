#Contestador de celular
num = str(int(input("ponga su numero de celular:")))
horallamada = int(input("a que hora hizo la llamada:"))
extraer_subcadena = num[5:8]
extraer_subcadena2 = num[0:3]
a = str("909")
b = str("877")

if horallamada >= 0 and horallamada <=7:
    print("contestar")

if horallamada>7 and horallamada<=14 and extraer_subcadena==a:
    print("contestar")
else:
    print("no contestar")
    
if horallamada>=17 and horallamada<=19:
    if extraer_subcadena2 == b:
        print("no contestas")
    else:
        print("contestas")
        
if horallamada>19:
    print("no contestas")
      