#Cálculo del dígito verificador de un rut
rut=int(input("introduzca su rut sin digito verificador porfavor: "))
s=(rut//10000000) * 3
t=((rut//1000000)%10) * 2
u=((rut//100000)%10) * 7
v=((rut//10000)%10) * 6
w=((rut//1000)%10) * 5
x=((rut//100)%10) * 4
y=((rut//10)%10) * 3
z=((rut//1)%10) * 2
plus=(s+t+u+v+w+x+y+z)
less_1= plus // 11
less_2= plus -(11*less_1)
less=11-less_2
if less == 11:
  print("dv=",end="")
  print(0)
elif less == 10:
  print("dv=",end="")
  print("k")
else:
  print("dv=",end="")
  print("dv=",less)