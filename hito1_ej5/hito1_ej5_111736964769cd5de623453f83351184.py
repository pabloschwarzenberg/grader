#Cálculo del dígito verificador de un rut
def f(x):
 return list(map(int, str(x)))

x=input("ingrese el numero")
n=int(x)
num=f(x)
nume=num[::-1]
cont=2
m=[]
for i in nume:
    z=int(i)
    if cont>7:
        cont=2
    y=cont*z
    cont+=1
    m.append(y)
r=0
for i in m:
    r+=i
modulo=r%11
digitoverificador=11-modulo
if digitoverificador==11:
    digitoverificador=0
if digitoverificador==10:
    digitoverificador="K"
print("dv=",digitoverificador)    