#Cálculo del dígito verificador de un rut
rut=int(input("ingrese su rut sin el digito verificador, ni puntos, ni el guion:"))
a=rut//100000000
b=((rut-a*100000000)//10000000)
c=((rut-a*100000000-b*10000000)//1000000)
d=((rut-a*100000000-b*10000000-c*1000000)//100000)
e=((rut-a*100000000-b*10000000-c*1000000-d*100000)//10000)
f=((rut-a*100000000-b*10000000-c*1000000-d*100000-e*10000)//1000)
g=((rut-a*100000000-b*10000000-c*1000000-d*100000-e*10000-f*1000)//100)
h=((rut-a*100000000-b*10000000-c*1000000-d*100000-e*10000-f*1000-g*100)//10)
i=((rut-a*100000000-b*10000000-c*1000000-d*100000-e*10000-f*1000-g*100-h*10)//1)
j=i*2
k=h*3
l=g*4
m=f*5
n=e*6
o=d*7
p=c*2
q=b*3
r=a*4
z=j+k+l+m+n+o+p+q+r
x=z%11
dv=11-x
if dv==11:
    print("dv=0")
elif dv==10:
    print("dv=k")
else: print("dv=",dv)

      