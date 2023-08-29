#Contestador de celular
nro = int(input("Ingrese un número: "))
hora = int(input("ingrese una hora: "))
telf= str(nro)

if hora>=0 and hora <=7 :
  print("CONTESTAR")
elif hora<14 and telf[-3:] == "909" :
  print("CONTESTAR")
elif hora >=17 and hora<=19 and telf[0:3] != "877":
  print("CONTESTAR")
elif hora > 19 :
  print("NO CONTESTAR")
else: 
  print("NO CONTESTAR")