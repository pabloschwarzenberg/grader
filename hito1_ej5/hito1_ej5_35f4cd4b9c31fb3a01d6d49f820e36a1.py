#Cálculo del dígito verificador de un rut
r=int(input("Ingrese el rut: "))

a=(r//10000000)*3
b=((r//1000000)%10)*2
c=((r//100000)%10)*7
d=((r//10000)%10)*6
e=((r//1000)%10)*5
f=((r//100)%10)*4
g=((r//10)%10)*3
h=((r//1)%10)*2
suma=(a+b+c+d+e+f+g+h)
res1= suma // 11
res2=suma-(11*res1)
res=11-res2
if res == 11:
  print("dv=",end="")
  print(0)
elif res == 10:
  print("dv=",end="")
  print("k")
else:
  print("dv=",end="")
  print(res)