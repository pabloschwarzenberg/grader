#Cálculo del dígito verificador de un rut
n=int(input("Ingrese rut sin guión: "))
a=n//10000000
b=(n-a*10000000)//1000000
c=(n-a*10000000-b*1000000)//100000
d=(n-a*10000000-b*1000000-c*100000)//10000
e=(n-a*10000000-b*1000000-c*100000-d*10000)//1000
f=(n-a*10000000-b*1000000-c*100000-d*10000-e*1000)//100
g=(n-a*10000000-b*1000000-c*100000-d*10000-e*1000-f*100)//10
h=(n-a*10000000-b*1000000-c*100000-d*10000-e*1000-f*100-g*10)//1

h=h*3
g=g*2
f=f*7
e=e*6
d=d*5
c=c*4
b=b*3
a=a*2
suma=a+b+c+d+e+f+g+h
suma=suma%11
valor=11-suma
if valor==11:
    print("dv=0")
elif valor==10:
    print("dv=K")
else:
    print("dv=",valor)
      