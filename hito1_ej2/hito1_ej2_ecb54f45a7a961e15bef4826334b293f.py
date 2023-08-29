#Contestador de celular
a=int(input("Ingrese numero telefonico:"))
b=int(input("Ingrese hora de la llamada:"))
if b>=0 and b<=7:
   print("CONTESTAR")
elif b>=7 and b<=14:
     if (((((a%10000000)%1000000)%100000)%10000)%1000)==909:
        print("CONTESTAR")
     else:
        print("NO CONTESTAR")
elif b>=17 and b<=19:
     if a//100000==877:
        print("NO CONTESTAR")
     else:
        print("CONTESTAR")
elif b>=19:
        print("NO CONTESTAR")