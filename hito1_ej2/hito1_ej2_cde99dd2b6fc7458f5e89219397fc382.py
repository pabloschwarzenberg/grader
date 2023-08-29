#Descomponer un número
hora = int(input("hora: ")) 
numero = int(input("numero telefonico: "))
ante_pe = str(numero//100%10)
penultimo = str(numero//10%10)
ultimo = str(numero%10)
terminal = ante_pe+penultimo+ultimo
if (hora>=0) and (hora <=7):
  print("CONTESTAR")
elif(hora<=14) and (terminal == "909"):
  print("CONTESTAR")
elif(hora>=15 and hora<=19):
  print("CONTESTAR")
else:
  print("NO CONTESTAR")