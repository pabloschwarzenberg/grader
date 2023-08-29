print("ingrese su RUT sin el numero verificado")
a=int(input("RUT:"))
b=int(a/10**7)
c=(int(a/10**6))%10
d=(int(a/10**5))%10
e=(int(a/10**4))%10
f=(int(a/10**3))%10
g=(int(a/10**2))%10
h=(int(a/10**1))%10
i=(int(a/10**0))%10
j=b*8
k=c*9
l=d*4
m=e*5
n=f*6
o=g*7
p=h*8
q=i*9
r=j+k+l+m+n+o+p+q
s=int((r%11)*10)/10
if s==10:
 t=str("k")
else:
 t=int(s)
print(str("dv="),t)
      