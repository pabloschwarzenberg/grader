#Contestador de celular
numero=input("Ingrese numero telefonico: ")
hora=int(input("Ingrese hora de llamada: "))

if 7>=hora>=0:
  print("CONTESTAR")
  
if 14>=hora>7:
  if (numero[5]=="9") and (numero[6]=="0") and (numero[7]=="9"):
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
    
if 19>hora>15:
  if numero[0]=="8":
    if numero[1]=="7":
      if numero[2]=="7":
        print("NO CONTESTAR")
  else:
    print("CONTESTAR")

if hora>19:
  print("NO CONTESTAR")
