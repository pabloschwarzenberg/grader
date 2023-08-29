#Contestador de celular
x= input("ingrese el numero del telefono")
if len(x)>8:
 print("numero",x,"invalido, intentelo nuevamente")
h= int(input("ingrese hora de llamada"))
if h>=0 and h<=7:
 print("contestar")
elif h<14:
 if x[-1]=='9' and x[-2]=='0' and x[-3]=='9' :
  print("contestar")
 else:
  print("no contestar")
elif h>=17 and h<=19 :
 if x[0]=='8' and x[1]=='7' and x[2]=='7' :
  print("no contestar")
elif h>19:
 print("no contestar")