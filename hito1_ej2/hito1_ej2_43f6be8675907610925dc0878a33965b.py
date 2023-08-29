#Contestador de celular
a=input("Ingrese numero telefonico:")
b=float(input("Ingrese hora de la llamada:"))


if 0<=b<=7:
  print("Resultado:CONTESTAR")
elif 7<=b<=14 and a[5:8]=="909":
  print("Resultado:CONTESTAR")
elif 15<=b<19 and a[0:3]!="877":
  print("Resultado:CONTESTAR")
else:
  print("Resultado:NO CONTESTAR")

  