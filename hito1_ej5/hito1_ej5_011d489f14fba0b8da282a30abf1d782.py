cdi=int(input("Escriba su rut: "))

x=(cdi//10000000) * 3

y=((cdi//1000000)%10) * 2

z=((cdi//100000)%10) * 7

d=((cdi//10000)%10) * 6

e=((cdi//1000)%10) * 5

f=((cdi//100)%10) * 4

g=((cdi//10)%10) * 3

h=((cdi//1)%10) * 2

suma=(x+y+z+d+e+f+g+h)

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