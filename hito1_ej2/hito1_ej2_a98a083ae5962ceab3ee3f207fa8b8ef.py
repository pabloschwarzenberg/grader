#Contestador de celular
a=int(input("Ingrese numero telefonico"))
b=int(input("Ingrese hora de la llamada"))

#b= str(a)
#primeros=b[:2]
#print(primeros)
#ultimos=b[2:]
#print(ultimos)

if 0<=b<=7:
    print('CONTESTAR')

elif b<=14:
     numero= str(a)
     ultimos=numero[5:]
     ultimos=int(ultimos)
     if ultimos==909:
         print("CONTESTAR")
     else:
         print("NO CONTESTAR")

elif 17<=b<=19:
    numero = str(a)
    primeros = numero[:3]
    primeros = int(primeros)
    if primeros==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

else:
    print("NO CONTESTAR")      