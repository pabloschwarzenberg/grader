#Contestador de celular
n=int(input("Ingrese numero telefonico: "))
h=int(input("Ingrese hora de la llamada: "))
f=n%1000
j=n//100000

if 0<=h<=7 :
   print("Resultado: CONTESTAR")
elif h<14:
   if f==909:
      print("Resultado: CONTESTAR")
   else:
      print("Resultado: NO CONTESTAR")

elif 17<=h<=19:
   if j==877:
       print("Resultado: NO CONTESTAR")
   
   else:
       print("Resultado: CONTESTAR")
elif 19>h:
   print("Resultado: NO CONTESTAR")
else:
   print("Resultado: NO CONTESTAR")
   


   
   