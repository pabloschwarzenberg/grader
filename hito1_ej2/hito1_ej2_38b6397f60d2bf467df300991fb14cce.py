#Contestador de celular
t=input("Ingrese numero telefonico")
h=int(input("Ingrese la hora de la llamada"))


if h>0 and h<7:
    print("CONTESTAR")
elif h>7 or h<14:
    if t[5]=="9" and t[6]=="0" and t[7]=="9":
        print ("CONTESTAR")
    else:
        print("NO CONTESTAR") 
    
        
elif h>=17 and h<=19:
    if t[5]=="8" and t[6]=="7" and t[7]=="7":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif h>19:
    print("NO CONTESTAR")
    
else:
    print("NO DISPONIBLE")      