#Cálculo del dígito verificador de un rut

rut=int(input("ingresa tu rut sin puntos: "))
a=(rut//10000000)

b=(rut//1000000)-(a*10)

c=(rut//100000)-(a*100)-(b*10)

d=(rut//10000)-(a*1000)-(b*100)-(c*10)

e=(rut//1000)-(a*10000)-(b*1000)-(c*100)-(d*10)

f=(rut//100)-(a*100000)-(b*10000)-(c*1000)-(d*100)-(e*10)

g=(rut//10)-(a*1000000)-(b*100000)-(c*10000)-(d*1000)-(e*100)-(f*10)

h=(rut%10)

hh=h*2
gg=g*3
ff=f*4
ee=e*5
dd=d*6
cc=c*7
bb=b*2
aa=a*3

verificador=aa+bb+cc+dd+ee+ff+gg+hh

verificador2=verificador%11
verificador3= 11-verificador2
if verificador3==11:
    print("dv=0",)
else:
    if verificador3==10:
        print("dv=k")
    else:
        print("dv=",str(verificador3))