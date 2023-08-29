#Contestador de celular
numero=(input("ingrerese numero telefonico de 8 cifras: "))
hora=int(input("ingrese hora de la llamada: "))
if hora>=0 and hora<=7:
  print("CONTESTAR")
elif hora<14:
    
    if numero[-1]=="9" and numero[-2]=="0"and numero[-3]=="9":
         print("CONTESTAR")
    else:
         print("NO CONTESTAR")
elif hora>=17 and hora<=19:
     if numero[0]=="8" and numero[1]=="7" and numero[2]=="7":
         print("NO CONTESTAR")
elif hora>19:
  print("NO CONTESTAR")

