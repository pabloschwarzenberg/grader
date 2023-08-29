#Contestador de celular
telefono=int(input("ingrese numero de celular: "))
hrs=int(input("ingrese hora de llamada: "))
telefono= str(telefono)
a=telefono[5:8]
e=telefono[0:3]
print("vector",a)
print("vector",e)
b=909
b=str(b)
c=877
c=str(c)
if ((0<=hrs>=7)):
   print("CONTESTAR") 
if (hrs>7 and hrs<=14 and telefono[5:8]==b):
   print("CONTESTAR")
else:
   print("NO CONTESTAR")
       
if hrs>=17 and hrs<=19:
   if telefono[3:0]== (c):
      print("vector inicia 877",telefono[3:0])
      print("NO CONTESTAR")
   else:
      print("CONTESTAR")