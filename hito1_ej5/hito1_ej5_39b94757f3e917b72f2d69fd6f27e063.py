#Cálculo del dígito verificador de un rut
rut=int(input(" rut: "))
a2=(rut//10000000) * 3

b2=((rut//1000000)%10) * 2

c2=((rut//100000)%10) * 7

d2=((rut//10000)%10) * 6

e2=((rut//1000)%10) * 5

f2=((rut//100)%10) * 4

g2=((rut//10)%10) * 3

h2=((rut//1)%10) * 2

suma=(a2+b2+c2+d2+e2+f2+g2+h2)

resto11= suma // 11

resto22=suma-(11*resto11)

resta=11-resto22

if resta == 11:

  print("dv=",end="")

  print(0)

elif resta == 10:

  print("dv=",end="")

  print("k")

else:

  print("dv=",end="")

  print("dv=",resta)      