#Descomponer un número
N=int(input())
D=[int(i) for i in str(N)]
if (len(D)==4):
  print("{}M+{}C+{}D+{}U".format(D[0],D[1],D[2],D[3]))
if (len(D)==3):
  print("{}C+{}D+{}U".format(D[0],D[1],D[2]))
if (len(D)==2):
  print("{}D+{}U".format(D[0],D[1]))
if (len(D)==1):
  print("{}U".format(D[0]))