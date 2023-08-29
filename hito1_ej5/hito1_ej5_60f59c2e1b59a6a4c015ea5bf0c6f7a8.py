#Cálculo del dígito verificador de un rut
rut=int(input('ingrese su rut sin puntos y sin el digito numerador:'))
a=rut%10
b=(rut%100)//10
c=(rut%1000)//100
x=(rut%10000)//1000
y=(rut%100000)//10000
z=(rut%1000000)//100000
m=(rut//1000000)%10
n=rut//10000000
op=(a*2)+(b*3)+(c*4)+(x*5)+(y*6)+(z*7)+(m*2)+(n*3)
res=op%11
di=11-res
if di==11:
    print('dv=',0)
elif di==10:
    print('dv=','k')
else:
    print('dv=',di)