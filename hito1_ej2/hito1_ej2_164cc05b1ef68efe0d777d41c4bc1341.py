#Contestador de celular
numero= int(input("marque numero de telefono:"))
hora= int(input("hora de llamada:"))
numerostr= str(numero)
numerolista= list(numerostr)
numerotupla= tuple(numerolista)
if 0<=hora<=7:
  print("CONTESTAR")
elif 7<hora<14:
  if numerotupla[5]=="9" and numerotupla[6]=="0" and numerotupla[7]=="9":
    print ("CONTESTAR")
  else:
    print ("NO CONTESTAR")
elif 14<=hora<17:
  print ("NO CONTESTAR")
elif 17<=hora<=19:
  if numerotupla[0]=="8" and numerotupla[1]=="7" and numerotupla[2]=="7":
    print ("NO CONTESTAR")
  else:
    print ("CONTESTAR")
else:
  print ("NO CONTESTAR")