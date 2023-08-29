#Contestador de celular
x =str(int(input("ingrese  numero de telefono:")))
y =int(input("ingrese hora de llamada:"))
extraer_subcadena =x[5:8]
extraer_subcadena2 =x[0:3]
s = str("909")
d = str("877")

if y >= 0 and y <=7:
    print("contestar")

if y > 7 and y <=14 and extraer_subcadena==s:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
    
if y >=17 and y <=19:
    if extraer_subcadena2 == d:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
        
if y > 19:
    print("NO CONTESTAR")