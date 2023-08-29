#Contestador de celular
numero=int(input("ingrese un numero de telefono "))
hora=int(input("ingrese su hora "))

if 0<hora<7 :
 print("contestar")
elif  7<hora<14 : 
  if numero%1000==909 :
   print("contestar")
  else :
    print("no contestar")
elif 17<hora<19 :
    if numero//100000==877 :
     print("no contestar")
    else :
        print("contestar")
else : 
    print("no contestar")      