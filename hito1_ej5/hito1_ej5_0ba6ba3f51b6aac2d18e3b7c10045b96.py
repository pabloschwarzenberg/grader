#Cálculo del dígito verificador de un rut
rut=int(input('ingresa tu rut, sin numero verificador:'))
a=(rut//10000000)
b=((rut//1000000)-10*a)
c=((rut//100000)-100*a-10*b)
d=((rut//10000)-1000*a-100*b-10*c)
e=((rut//1000)-10000*a-1000*b-100*c-10*d)
f=((rut//100)-100000*a-10000*b-1000*c-100*d-10*e)
g=((rut//10)-1000000*a-100000*b-10000*c-1000*d-100*e-10*f)
h=((rut//1)-10000000*a-1000000*b-100000*c-10000*d-1000*e-100*f-10*g)
#print(a,b,c,d,e,f,g,h)
aa=a*3
bb=b*2
cc=c*7
dd=d*6
ee=e*5
ff=f*4
gg=g*3
hh=h*2
#print(aa,bb,cc,dd,ee,ff,gg,hh)
suma=aa+bb+cc+dd+ee+ff+gg+hh
#print(suma)
z=int(suma/11)
#print(z)
x=int(suma-(z*11))
#print(x)
y=int(11-x)
if y>=1 and y<=9:
        print('dv=',y)
elif y==10:
        print('dv=',str('k'))
elif y==11:
        print('dv=',str('0'))



