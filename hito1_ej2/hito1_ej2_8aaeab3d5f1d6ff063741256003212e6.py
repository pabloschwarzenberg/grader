#Contestador de celular
num= str(input("ingrese el numero entrante:"))
hr= int(input("ingrese la hora de la llamada:"))
n = num[5:9]
m = num[0:3]
int(n)
int(m)
if (hr)<=(7):
  print("contestar")
  
elif (hr)<=(14):
   if (n==909):
     print("contestar")
   else:
       print("contestar")
       
elif (hr)==(17,18,19):
   if (m==877):
     print("no contestar")
   else:
       print("contestar")
       
else:
    print("no contestar")
   