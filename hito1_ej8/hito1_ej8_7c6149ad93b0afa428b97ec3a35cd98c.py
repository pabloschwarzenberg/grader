#Descomponer un número
num=int(input("Ingrese un número:"))
suma=""
dm=num//1000
c=(num-(dm*1000))//100
d=(num-(dm*1000)-(c*100))//10
u=(num-(dm*1000)-(c*100)-(d*10))
if dm!=0:
    suma=str(dm)+"M"+" + "+str(c)+"C"+" + "+str(d)+"D"+" + "+str(u)+"U"
if dm==0:
    suma=str(c)+"C"+" + "+str(d)+"D"+" + "+str(u)+"U"
if dm==0 and c==0:
    suma=str(d)+"D"+" + "+str(u)+"U"
if dm==0 and c==0 and d==0:
    suma=str(u)+"U"
print(suma)