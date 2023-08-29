#Cálculo del dígito verificador de un rut
r = int(input(" rut: "))
x=(r//10000000)*3
y=((r//1000000)%10)*2
z=((r//100000)%10)*7
f=((r//10000)%10)*6
g=((r//1000)%10)*5
h=((r//100)%10)*4
i=((r//10)%10)*3
j=((r//1)%10)*2
suma=(x+y+z+f+g+h+i+j)
resto=suma//11
resto2=suma-(11*resto)
resta=11-resto2
if resta==11:
  print("dv=",end="")
  print(0)
elif resta == 10:
  print("dv=",end="")
  print("k")
else:
  print("dv=",end="")
  print("dv=",resta)