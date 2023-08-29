#Cálculo del dígito verificador de un rut
rut=int(input("Cual es el rut: "))

x=(rut//10000000) * 3

c=((rut//1000000)%10) * 2

v=((rut//100000)%10) * 7

b=((rut//10000)%10) * 6

n=((rut//1000)%10) * 5

m=((rut//100)%10) * 4

l=((rut//10)%10) * 3

k=((rut//1)%10) * 2

su=(x+c+v+b+n+m+l+k)

resto1= su // 11

resto2=su-(11*resto1)

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
      