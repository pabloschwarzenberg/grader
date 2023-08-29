n = input("ingrese un numero")
r = len(n)
if r== 4:
  print(n[0]+"M +"+n[1] + "C +"+n[2]+ "D +"+n[3]+ "U")
elif r==3:
  print(n[0] + "C +"+n[1]+ "D +"+n[2]+ "U")
elif r==2:
  print(n[0]+ "D +"+n[1]+ "U")
elif r==1:
  print(n[0]+ "U")