tel = input("Ingrese numero telefonico: ")
hora = int(input("Ingrese hora de la llamada: "))
 
if hora >= 0 and hora <=7:
    print("CONTESTAR")
elif hora<14 and tel[5]=="9" and tel[6]=="0" and tel[7]=="9":
    print("CONTESTAR")
elif hora<14:
    print("NO CONTESTAR")
elif hora>= 17 and hora<= 19  and tel[0]=="8" and tel[1]=="7" and tel[2]=="7":
    print("NO CONTESTAR")
elif hora>= 17 and hora<=19:
    print("CONTESTAR")
elif hora>19:
    print("NO CONTESTAR")