#Cálculo del dígito verificador de un rut
r=int(input("Escriba su rut: "))
a=(r//10000000)
b=(r//1000000)%10
c=(r//100000)%10
d=(r//10000)%10
e=(r//1000)%10
f=(r//100)%10
g=(r//10)%10
h=(r//1)%10 


ai=a*3
bi=b*2
ci=c*7
di=d*6
ei=e*5
fi=f*4
gi=g*3
hi=h*2

prod_sum = ai+bi+ci+di+ei+fi+gi+hi

rest=prod_sum//11
resta=prod_sum-(11*rest)
dv=11-resta

if dv==11:
    print("dv=0")
elif dv==10:
    print("dv=k")
else:
    print("dv=", dv)





