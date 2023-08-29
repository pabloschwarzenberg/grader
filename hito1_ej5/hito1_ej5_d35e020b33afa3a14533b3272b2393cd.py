rut=int(input("Ingresa tu rut sin digito verificador:"))
a=rut//10000000
b=(rut//1000000)%10
c=(rut//100000)%10
d=(rut//10000)%10
e=(rut//1000)%10
f=(rut//100)%10
g=(rut//10)%10
h=rut%10
miau=h*2
guau=g*3
pio=f*4
mu=e*5
bee=d*6
cuak=c*7
kikiriki=b*2
que=a*3
suma=miau+guau+pio+mu+bee+cuak+kikiriki+que
caca=suma//11
coni=suma - (11*caca)
nacha=11-coni
if nacha==11:
    print("dv=0")
elif nacha==10:
    print("dv=k")
else:
    print("dv=",nacha)