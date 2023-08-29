#Cálculo del dígito verificador de un rut
x=int(input('Ingresa tu rut sin puntos ni guion'))
a=(x%10)*2
b=((x//10)%10)*3
c=((x//100)%10)*4
d=((x//1000)%10)*5
e=((x//10000)%10)*6
f=((x//100000)%10)*7
g=((x//1000000)%10)*2
h=((x//10000000)%10)*3

S=a+b+c+d+e+f+g+h
A=S%11
B=11-A
if B==11:
        print('dv=','0')
if B==10:
        print('dv=','K')
if B<10:
        print('dv=',B)
