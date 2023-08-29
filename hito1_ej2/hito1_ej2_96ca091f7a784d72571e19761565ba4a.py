#Contestador de celular
num=int(input("ingrese num"))
hora=int(input("ingrese hora"))
if 7>hora>=0:
  print("CONTESTAR")
elif 14>hora>=7 and num%1000==909:
  print("CONTESTAR")
elif 17>hora>=14 and num%1000!=877:
  print("CONTESTAR")
else:
  print("NO CONTESTAR")