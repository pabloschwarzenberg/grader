#Contestador de celular
num= input ("ingrese un numero de telefono")
hora= float (input ("ingrese la hora de la llamada"))
lista=[num]
if 0 < hora and hora <=7 :
   print ("contestar")
elif hora< 14 and hora >7:
     if num [5] =="9" and num[6]=="0" and num [7]=="9" :
        print ("contestar")
     else:
         print ("no contestar")
elif 17< hora and hora <19:
  if num[0]== "8" and num [1]=="7" and num [2]=="7" :
        print ("no contestar")
else:
         print ("no contestar")