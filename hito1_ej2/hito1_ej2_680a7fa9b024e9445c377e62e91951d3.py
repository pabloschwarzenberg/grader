#Contestador de celular
N=input("Ingrese numero telefonico:")
H=int(input("Ingrese hora de la llamada:"))
if 0<=H<=7 :
  print("CONTESTAR")
elif 7<H<14 and int(N[5])==9 and int(N[6])==0 and int(N[7])==9 :
    print("CONTESTAR")
elif 17<=H<=19 and int(N[0])!=8 and int(N[1])!=7 and int(N[2])!=7 :
  print("CONTESTAR")
else:
  print("NO CONTESTAR")
