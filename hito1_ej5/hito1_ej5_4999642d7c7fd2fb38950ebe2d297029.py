#Cálculo del dígito verificador de un rut from itertools import cycle
run=int(input("Ingrese el run: "))
a=(run//10000000) * 3
b=((run//1000000)%10) * 2
c=((run//100000)%10) * 7
d=((run//10000)%10) * 6
e=((run//1000)%10) * 5
f=((run//100)%10) * 4
g=((run//10)%10) * 3
h=((run//1)%10) * 2
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