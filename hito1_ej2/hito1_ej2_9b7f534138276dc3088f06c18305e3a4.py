#Contestador de celular
n=int(input("Ingrese numero telefonico: "))
h=int(input("Ingrese hora de la llamada: "))
if 0<h and h<7:
    print("CONTESTAR")
elif h<14:
    if n%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif h>17 and h<19:
    if 87700000<=n and n<=87800000:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
    
    
          