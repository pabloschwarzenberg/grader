#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese el rut: "))
m=(rut//10000000) * 3
n=((rut//1000000)%10) * 2
b=((rut//100000)%10) * 7
v=((rut//10000)%10) * 6
c=((rut//1000)%10) * 5
x=((rut//100)%10) * 4
z=((rut//10)%10) * 3
l=((rut//1)%10) * 2
suma=(m+n+b+v+c+x+z+l)
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