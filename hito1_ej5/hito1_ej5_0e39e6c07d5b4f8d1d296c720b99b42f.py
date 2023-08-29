#Cálculo del dígito verificador de un rut
rut=int(input("ingrese rut:"))
a=(rut%10)
aa=a*2
b=((rut%10**2-a)//10)
bb=b*3
c=((rut%10**3-b)//10**2)
cc=c*4
d=((rut%10**4-c)//10**3)
dd=d*5
e=((rut%10**5-d)//10**4)
ee=e*6
f=((rut%10**6-e)//10**5)
ff=f*7
g=((rut%10**7-f)//10**6)
gg=g*2
h=((rut%10**8-g)//10**7)
hh=h*3
mama=aa+bb+cc+dd+ee+ff+gg+hh
print(mama)
papa=mama//11
print(papa)
tutu=mama-(11*papa)
print(tutu)
dv= 11-tutu
if dv==11:
   print("dv=0")
elif dv==10:
     print("dv=k")
else:
     print("dv=",dv)

