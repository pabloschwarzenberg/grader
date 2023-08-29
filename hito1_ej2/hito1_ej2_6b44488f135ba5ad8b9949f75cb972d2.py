#Contestador de celular
nt=int(input("Ingrese numero telefonico: "))
hr=int(input("Ingrese hora de la llamada: "))
if 19<hr<=23:
  print("NO CONTESTAR")
if 15<=hr<=16:
  print("NO CONTESTAR")
if 0<=hr<=7:
  print("CONTESTAR")
if 8<=hr<=14:
  if str(nt)[5]=="9" and str(nt)[6]=="0" and str(nt)[7]=="9":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
if 17<=hr<=19:
  if str(nt)[0]=="8" and str(nt)[1]=="7" and str(nt)[2]=="7":
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")