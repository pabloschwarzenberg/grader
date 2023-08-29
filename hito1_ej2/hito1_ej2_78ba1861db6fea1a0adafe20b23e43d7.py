#Contestador de celular
NT=int(input("Ingrese un numero telefonico de 8 digitos: "))
H=int(input("Ingrese hora de 0 a 23 horas: "))
NTtexto=str(NT)

if H>=0 and H<=7:
  print("Contestar")
elif H<=14 and NTtexto.find("909")==5:
  print("Contestar")
elif H>=17 and H<=19:
    if NTtexto.find("877")==0:
          print("NO CONTESTAR")
    else: print("NO CONTESTAR")
else:
    print("NO CONTESTAR")