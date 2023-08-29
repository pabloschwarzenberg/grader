#Cálculo del dígito verificador de un rut
num=int(input("Ingrese su rut: "))
a=(num//10000000) * 3
b=((num//1000000)%10) * 2
c=((num//100000)%10) * 7
d=((num//10000)%10) * 6
e=((num//1000)%10) * 5
w=((num//100)%10) * 4
z=((num//10)%10) * 3
q=((num//1)%10) * 2
suma = (a+b+c+d+e+w+z+q)
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