#Sistema de Ecuaciones
a1=float(input())
b1=float(input())
c1=float(input())
a2=float(input())
b2=float(input())
c2=float(input())
caca=c2/a2
caca2=-b2/a2
tata=c1/a1
tata2=-b1/a1
res1=tata-caca
res2=caca2-tata2
yr=round(res1/res2,1)
xr=round(caca+caca2*yr,1)
print("x="+str(xr))
print("y="+str(yr))
