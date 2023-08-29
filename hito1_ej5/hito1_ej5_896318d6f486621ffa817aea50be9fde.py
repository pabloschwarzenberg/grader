#Cálculo del dígito verificador de un rut
Rut_persona=int(input("Ingrese su rut: "))

q=(Rut_persona//10000000) * 3

w=((Rut_persona//1000000)%10) * 2

e=((Rut_persona//100000)%10) * 7

r=((Rut_persona//10000)%10) * 6

t=((Rut_persona//1000)%10) * 5

y=((Rut_persona//100)%10) * 4

u=((Rut_persona//10)%10) * 3

i=((Rut_persona//1)%10) * 2

Sumar=(q+w+e+r+t+y+u+i)

Resto_1= Sumar // 11

Resto_2= Sumar-(11*Resto_1)

resta= 11-Resto_2

if resta == 11:

  print("dv=",end="")

  print(0)

elif resta == 10:

  print("dv=",end="")

  print("K")

else:

  print("dv=",end="")

  print(resta)