#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese rut sin dv: "))
a=rut//10000000
b=(rut//1000000)%10
c=(rut//100000)%10
d=(rut//10000)%10
e=(rut//1000)%10
f=(rut//100)%10
g=(rut//10)%10
h=(rut//1)%10
w=h*2+g*3+f*4+e*5+d*6+c*7+b*2+a*3
x=w%11
y=11-x

if y==11:
    print("dv=0")
elif y==10:
    print("dv=k")
else:
    print("dv=",y)
      