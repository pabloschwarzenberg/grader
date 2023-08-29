rut=int(input("Favor ingrese numero de rut a consultar: "))

a=((rut//1000000)%10) * 2

b=(rut//10000000) * 3

c=((rut//100)%10) * 4

d=((rut//1)%10) * 2

e=((rut//1000)%10) * 5

f=((rut//100000)%10) * 7

g=((rut//10)%10) * 3

h=((rut//10000)%10) * 6

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