#Cálculo del dígito verificador de un rut
rut=int(input("adjunte su rut: "))

H=(rut//10000000) * 3

F=((rut//1000000)%10) * 2

K=((rut//100000)%10) * 7

Z=((rut//10000)%10) * 6

C=((rut//1000)%10) * 5

T=((rut//100)%10) * 4

P=((rut//10)%10) * 3

M=((rut//1)%10) * 2

suma=(H+F+K+Z+C+T+P+M)

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