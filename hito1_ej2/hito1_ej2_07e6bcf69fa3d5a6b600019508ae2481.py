n = int(input("Ingrese su numero telefonico"))
h = int (input("Ingrese hora de la llamada: "))
numero_str= str(n)
if 0<=h<=7:
    print ("CONTESTAR")
elif 7<h<14:
    if numero_str[5:8]=="909":
     print ("CONTESTAR")
    else:
     print ("NO CONTESTAR")
elif  14<=h<17:
 print ("NO CONTESTAR")
elif 17<=h<=19:

    if numero_str[0:3]=="877" :

     print ("NO CONTESTAR")
    else:
     print ("CONTESTAR" )
elif h>19:
 print("NO CONTESTAR")