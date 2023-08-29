#Contestador de celular
N=int(input("Ingrese numero telefonico:"))
H=int(input("Ingrese hora de la llamada:"))
if (0<=H<=7) or (H<14 and (N-909)%1000==0) or (17<H<19 and not(87700000<N<87799999)):
  print("CONTESTAR")
else:
  print("NO CONTESTAR")
  #n-909%1000==0