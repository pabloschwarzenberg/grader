#Contestador de celular
n=int(input("ingrese numero de telefono:"))
h=int(input("ingrese hora:"))
if 0<=h<=7:
    print("CONTESTAR")
elif 7<h<=14 and n%1000!=909:
    print("NO CONTESTAR")
elif 7<h<=14 and n%1000==909:
    print("CONTESTAR")
elif 17<=h<=19 and n//100000!=877:
    print("CONTESTAR")
elif 17<=h<=19 and n//100000==877:
    print("NO CONTESTAR")
elif h>19:
    print("NO CONTESTAR")
    
  