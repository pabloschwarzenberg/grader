#Cálculo del dígito verificador de un rut
num=int(input("Ingrese su rut: "))
z=(num//10000000) * 3
x=((num//1000000)%10) * 2
c=((num//100000)%10) * 7
v=((num//10000)%10) * 6
b=((num//1000)%10) * 5
n=((num//100)%10) * 4
m=((num//10)%10) * 3
a=((num//1)%10) * 2
suma = (z+x+c+v+b+n+m+a)
restante = suma // 11
restante1 = suma-(11 * restante)
menos= 11 - restante1
if menos == 11:
  print('dv=',end ='')
  print (0)
elif menos == 10:
  print ('dv=',end ='')
  print ('k')
else:
  print ('dv=',end ='')
  print (menos)      