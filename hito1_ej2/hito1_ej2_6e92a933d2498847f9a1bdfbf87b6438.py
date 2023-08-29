#Contestador de celular
nro=int(input("Ingrese numero telefonico:"))
hora=int(input("Ingrese hora de la llamada:"))
contestar=False
if(hora<=7 and hora>=0):
  contestar=True
elif(hora>7 and hora<14):
  if(nro%1000==909):
    contestar=True
if(hora>17 and hora<19 and (nro-nro%100000)!=87700000):
    contestar=True

if(contestar):
  print("Resultado: CONTESTAR")
else:
  print("Resultado: NO CONTESTAR")
  