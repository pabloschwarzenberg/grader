a = int(input('Ingrese su rut: '))

A=a//10000000
n=a%10000000
B=n//1000000
n=n%1000000
C=n//100000
n=n%100000
D=n//10000
n=n%10000
E=n//1000
n=n%1000
F=n//100
n=n%100
G=n//10
n=n%10

suma=A*3 + B*2 + C*7 + D*6 + E*5 + F*4 + G*3 +n*2

division= suma/11
resto=suma%11
total=11-resto
if total ==11:
  print('dv=0')
elif total==10:
  print('dv=k')
else:
  print('dv=',total)