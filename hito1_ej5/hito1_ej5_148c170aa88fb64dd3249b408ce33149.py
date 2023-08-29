#Cálculo del dígito verificador de un rut
print("Verificador del RUT")
rut=int(input("Ingrese su rut de siete digitos:"))
a=(rut//10000000) * 3
b=((rut//1000000)%10) * 2
c=((rut//100000)%10) * 7
d=((rut//10000)%10) * 6
e=((rut//1000)%10) * 5
f=((rut//100)%10) * 4
g=((rut//10)%10) * 3
h=((rut//1)%10) * 2
suma=(a+b+c+d+e+f+g+h)
division= suma // 11
resta=suma-(11*division)
division=11-resta
if division == 11:
  print("dv=0")
elif division == 10:
  print("dv=k")
else:
  print("dv=",division)