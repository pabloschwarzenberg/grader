#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese el rut: "))
U = (rut//10000000) * 3
D = ((rut//1000000)%10) * 2
T = ((rut//100000)%10) * 7
C = ((rut//10000)%10) * 6
CI = ((rut//1000)%10) * 5
S = ((rut//100)%10) * 4
SI = ((rut//10)%10) * 3
O = ((rut//1)%10) * 2
suma=(U + D + T + C + CI + S + SI + O)
resto1= suma // 11
resto2=suma-(11*resto1)
resta=11-resto2
if resta == 11:
  print("dv=",end="")
  print(0)
elif resta == 10:
  print("dv=",end="")
  print("k")
else:
  print("dv=",end="")
  print(resta)