#Contestador de celular
N=input("Ingrese numero telefonico: ")
H=int(input("Ingrese hora de la llamada: "))

if 0<=H<=7:
 print("Resultado: CONTESTAR")
elif 7<H<=14 and int(N[5:])==909:
  print("Resultado: CONTESTAR")
elif 7<H<=14 and int(N[5:])!=909:
    print("Resultado: NO CONTESTAR")
elif 17<H<=19 and int(N[0:3])==877:
  print("Resultado: NO CONTESTAR")
elif 17<H<=19 and int(N[0:3])!=877:
    print("Resultado: CONTESTAR")
elif 19<H:
  print("Resultado: NO CONTESTAR")