#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su rut: "))

n=(rut//10000000) * 3

m=((rut//1000000)%10) * 2

l=((rut//100000)%10) * 7

o=((rut//10000)%10) * 6

p=((rut//1000)%10) * 5

q=((rut//100)%10) * 4

r=((rut//10)%10) * 3

s=((rut//1)%10) * 2

suma=(n+m+l+o+p+q+r+s)

minus1= suma // 11

minus2=suma-(11*minus1)

minus=11-minus2

if minus == 11:

  print("dv=",end="")

  print(0)

elif minus == 10:

  print("dv=",end="")

  print("k")

else:

  print("dv=",end="")

  print(minus) 