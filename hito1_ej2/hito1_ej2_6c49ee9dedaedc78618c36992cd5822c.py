#Contestador de celular
numero = str(int(input("Ingrese un numero de telefono: ")))
hora = int(input("ingrese hora: "))
exc = numero [5:8]
exc2 = numero [8:3]
x = str("909")
y = str("877")

if 0 <= hora <= 7:
    print("CONTESTAR")

if 7 < hora < 14 and exc == x:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
    
if 17 <= hora <= 19 and exc == y:
    print("NO CONTESTAR")
else:
    print("CONTESTAR")

if hora > 19:
    print("NO CONTESTAR")