#Cálculo del dígito verificador de un rut
n=eval(input('Ingrese su n: '))

a=n%10     
n=n//10   

b=n%10
n=n//10

c=n%10
n=n//10

d=n%10
n=n//10

e=n%10
n=n//10

f=n%10
n=n//10

g=n%10
n=n//10

h=n%10

sd=(a*2+b*3+c*4+d*5+e*6+f*7+g*2+h*3)

dd=(sd//11)

rdd=(sd-(11*dd))

dv=(11-rdd)

if dv==11:
    print('dv= ','0')

if dv==10:
    print('dv= ','k')

else:
    print('dv=', dv)

