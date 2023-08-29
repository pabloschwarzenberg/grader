#Contestador de celular
n=int(input("ingrese numero telefonico:"))
h=int(input("ingrese hora de la llamada:",))

if n/10000000 < 1:
    print ("el numero debe ser de 8 cifras")

if 0<=h<=7:
        print("CONTESTAR")

if 7<h<14:

    if n%1000 == 909:   
            print("CONTESTAR")
    else:
            print("NO CONTESTAR")

if 17<=h<=19:
        
        if n // 100000 != 877:
             print("CONTESTAR")
        else:
             print("NO CONTESTAR")
if 19<h<=23:
         print("NO CONTESTAR")
if 14<=h<17:
    
     print("NO CONTESTAR")
      