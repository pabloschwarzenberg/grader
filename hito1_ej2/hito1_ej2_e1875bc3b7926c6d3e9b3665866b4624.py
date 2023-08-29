#Contestador de celular
y=int(input("ingrese numero telefonico:",))
x=int(input("ingrese hora de llamada:",))

if 0<=x<=7:
    print("CONTESTAR")

if 7<x<=14:
   if y-(((y//1000))*1000)==909:
      print("CONTESTAR")

   else:
        print("NO CONTESTAR")

if 14<x<17:
    print("NO CONTESTAR")

if 17<=x<=19:
    if(y//100000)==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

if 19<x<=23:

    print("NO CONTESTAR")
