rut=int(input("Ingrese el rut: "))

a=(rut//10000000) * 3

b=((rut//1000000)%10) * 2

c=((rut//100000)%10) * 7

d=((rut//10000)%10) * 6

e=((rut//1000)%10) * 5

f=((rut//100)%10) * 4

g=((rut//10)%10) * 3

h=((rut//1)%10) * 2

suma=(a+b+c+d+e+f+g+h)

resta= suma // 11

resta1=suma-(11*resta)

restaa=11-resta1

if restaa == 11:

  print("dv=",end="")

  print(0)

elif restaa == 10:

  print("dv=",end="")

  print("k")

else:

  print("dv=",end="")

  print(restaa)
      