#Contestador de celular
      #Contestador de celular
n=int(input("ingrese numero telefonico de 8 digitos: "))
hora=int(input("ingrese la hora: "))

if 0<=hora<=7:
    print("CONTESTAR")
if 7<hora<14:
     if(n%1000)==909:
        print("CONTESTAR")
     else:
        print("NO CONTESTAR")
if 14<=hora<17:
    print("CONTESTAR")
if 17<=hora<=19:
    if(n//100000)==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if 19<hora:
    print("NO CONTESTAR")
    