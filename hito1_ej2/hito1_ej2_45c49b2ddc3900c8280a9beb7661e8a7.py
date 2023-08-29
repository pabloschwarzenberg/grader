#Contestador de celular
nro=input("Ingrese número telefonico: ")
hra=int(input("Ingrese hora de la llamada: "))
ultimos3=extraer_subcadena=nro[5:8]
primeros3=estraer_subcadena=nro[0:3]
if(hra>0 and hra<7):
  print("CONTESTAR")
if(ultimos3=="909"):
    print("CONTESTAR")
elif(hra<14):
  print("NO CONTESTAR")
if(primeros3=="877"):
  print("NO CONTESTAR")
elif(hra>17 and hra<19):
  print("CONTESTAR")
if(hra>19):
  print("NO CONTESTAR")