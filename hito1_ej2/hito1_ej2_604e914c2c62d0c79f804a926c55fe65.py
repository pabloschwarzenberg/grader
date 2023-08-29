#Contestador de celular
n=int(input("Ingrese numero telefonico:"))
h=int(input("ngrese hora de la llamada:"))
n=str(n)
if 0<=h<=7:
  print("CONTESTAR")
if 7<h<=14 and int(n[5])==9 and int(n[6])==0 and int(n[7])==9:
  print("CONTESTAR")
else:
    print("NO CONTESTAR")
if 14<h<17:
  print("NO CONTESTAR")
if 17<=h<=19 and int(n[5])==8 and int(n[6])==7 and int(n[7])==7:
  print("NO CONTESTAR")
else:
    print("CONTESTAR")
if 19<h<=23:
  print("NO CONTESTAR")