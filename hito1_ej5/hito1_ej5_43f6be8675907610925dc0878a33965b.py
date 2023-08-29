#Cálculo del dígito verificador de un rut
rut=input()
if len(rut)==7:
  rut="0"+rut
a=rut[0]
b=rut[1]
c=rut[2]
d=rut[3]
e=rut[4]
f=rut[5]
g=rut[6]
h=rut[7]

a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
g=int(g)
h=int(h)

l=a*3
m=b*2
n=c*7
ñ=d*6
o=e*5
p=f*4
q=g*3
r=h*2
i=l+m+n+ñ+o+p+q+r
j=i%11
k=11-j
if(k==10):
   print("dv=k")
elif(k==11):
   print("dv=0")
else:
   print("dv=",k) 