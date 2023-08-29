numero=str(input("Ingrese numero telefonico: ")) 
Hora=int(input("Ingrese hora de la llamada: "))

if Hora<=7 and Hora>=0:
    print("CONTESTAR")
    
elif Hora<14 and Hora>7 and numero[5]=="9" and numero[6]=="0" and numero[7]=="9": 
    print("CONTESTAR")
    
elif Hora<14 and Hora>7 and (numero[5]!="9" or numero[6]!="0" or numero[7]!="9"):
    print("NO CONTESTAR")

elif Hora<17 and Hora>=14:
    print("NO CONTESTAR")

elif Hora<=19 and Hora>=17 and numero[5]=="8" and numero[6]=="7" and numero[7]=="7":
    print("NO CONTESTAR")
    
elif Hora<=19 and Hora>=17 and (numero[5]!="8" or numero[6]!="7" or numero[7]!="7"):
    print("NO CONTESTAR")

elif Hora>19:
    print("NO CONTESTAR")
