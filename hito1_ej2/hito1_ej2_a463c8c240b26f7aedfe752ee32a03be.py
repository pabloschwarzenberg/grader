#Contestador de celular
print("ingrese su numero telefonico: ")
numerotelefonico = int(input())
print("ingrese la hora en que comienza la llamada: ")
hora = int(input())
sos = numerotelefonico%1000
if hora >= 0 and hora <= 7:
    print("CONTESTAR")
if hora > 7 and hora <= 14 and sos == 909:
    print("CONTESTAR")
if hora > 7 and hora <= 14 and sos != 909:
    print("NO CONTESTAR")
if hora > 14 and hora <17:
    print("NO CONTESTAR")
if hora >= 17 and hora < 19 and numerotelefonico > 87699999 and numerotelefonico < 87800000:
    print("NO CONTESTAR")
if hora >= 17 and hora <= 19 and numerotelefonico < 87699999 and numerotelefonico > 87800000:
    print("CONTESTAR")
if hora > 19:
    print("NO CONTESTAR")      