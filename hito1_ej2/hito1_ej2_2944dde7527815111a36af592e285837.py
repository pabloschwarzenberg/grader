#Contestador de celular
numero = int(input("ingrese numero telefonico:"))
hora = int(input("ingrese hora de la llamada:"))
c= str(numero)
d= c[5:8]
f= int(d) 
e= c[1:3]
g= int(e)


if (f==909):
    print("CONTESTAR")
else:
     print("NO CONTESTAR")

if (g==877):
    print("NO CONTESTAR")
else:
    print("CONTESTAR")

if hora<=7:
    print("CONTESTAR")
elif hora>14:
    print("NO CONTESTAR")
elif hora==17:
    print("CONTESTAR")
elif hora==18:
    print("CONTESTAR")
elif hora==19:
    print("CONTESTAR")
