#Contestador de celular
numero=int(input("Ingrese su numero telefonico: "))
hora=int(input("Ingrese la hora de llamada: "))

c=numero/1000
d=numero/100000

if((0<=hora<=7)):
    print("CONTESTAR")

if((7<hora<14)and((c-int(c))==0.909)):
    print("CONTESTAR")
else:
   if(7<hora<14):
     print("CONTESTAR")

if(14<=hora<17):
    print("CONTESTAR")

if((17<=hora<=19)and(int(d)==877)):
    print("NO CONTESTAR")
else:
   if(17<=hora<=19):
      print("CONTESTAR")

if(19<hora):
    print("NO CONTESTAR")