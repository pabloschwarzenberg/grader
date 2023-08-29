#Descomponer un número
n = str(input("Numero a descomponer: "))
if len(n) == 1:
  print("{}U".format(n))
elif len(n) == 2:
  print("{}D + {}U".format(n[0],n[1]))
elif len(n) == 3:
  print("{}C + {}D + {}U".format(n[0],n[1],n[2]))
elif len(n) == 4:
  print("{}M + {}C + {}D + {}U".format(n[0],n[1],n[2],n[3]))