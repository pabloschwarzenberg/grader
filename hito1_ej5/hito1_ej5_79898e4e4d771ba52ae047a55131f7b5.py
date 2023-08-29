variableRut=int(input("Ingrese el rut: "))

a=(variableRut//10000000) * 3

b=((variableRut//1000000)%10) * 2

c=((variableRut//100000)%10) * 7

d=((variableRut//10000)%10) * 6

e=((variableRut//1000)%10) * 5

f=((variableRut//100)%10) * 4

g=((variableRut//10)%10) * 3

h=((variableRut//1)%10) * 2

suma=(a+b+c+d+e+f+g+h)

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