#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese el rut: "))
j=(rut//10000000) * 3
k=((rut//1000000)%10) * 2
l=((rut//100000)%10) * 7
m=((rut//10000)%10) * 6
n=((rut//1000)%10) * 5
x=((rut//100)%10) * 4
y=((rut//10)%10) * 3
z=((rut//1)%10) * 2
suma=(j+k+l+m+n+x+y+z)
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