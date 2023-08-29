#Contestador de celular
a=int(input("ingrese su numero de telefono(maximo ocho cifras): "))
b=int(input("ingrese la hora de llamada: "))
c=("CONTESTAR")
e=("NO CONTESTAR")
if 0<=b<=7:
 print(c) 
elif b<14 and 90900000<=a<=90999999:
 print(e) 
elif 8<b<14 and a%1000==909 :
 print(c) 
elif 17<=b<=19 and 877==a//100000:
 print(e)
elif 19<b:
 print(e)    