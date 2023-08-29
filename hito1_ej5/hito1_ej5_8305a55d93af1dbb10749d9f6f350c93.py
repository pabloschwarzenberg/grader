#Cálculo del dígito verificador de un rut
x=int(input("Por favor ingrese su rut :  "))
n=x
a=(n//10000000)*3
n=x%10000000
b=(n//1000000)*2
n=x%1000000
c=(n//100000)*7
n=x%100000
d=(n//10000)*6
n=x%10000
e=(n//1000)*5
n=x%1000
f=(n//100)*4
n=x%100
g=(n//10)*3
h=(x%10)*2
suma=(a+b+c+d+e+f+g+h)//11
suma2=(a+b+c+d+e+f+g+h)-(11*suma)
suma3=11-suma2
if suma3==11:
    print("dv=0")
elif suma3==10:
    print("dv=K")
else:
    print("dv=",suma3)     