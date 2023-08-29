#Cálculo del dígito verificador de un rut
n=int(input("ingresa tu rut sin el digito verificador: "))

a=n//10000000
b=n//1000000-(a*10)
c=n//100000-(a*100+b*10)
d=n//10000-(a*1000+b*100+c*10)
e=n//1000-(a*10000+b*1000+c*100+d*10)
f=n//100-(a*100000+b*10000+c*1000+d*100+e*10)
g=n//10-(a*1000000+b*100000+c*10000+d*1000+e*100+f*10)
i=n-(a*10000000+b*1000000+c*100000+d*10000+e*1000+f*100+g*10)

j=i*2
k=g*3
l=f*4
m=e*5
n=d*6
o=c*7
p=b*2
q=a*3

x=j+k+l+m+n+o+p+q

y=x//11
w=x-(11*y)
z=11-w

if z==11:
    print("dv= 0")
elif z==10:
    print("dv= K")
else:
    print("dv= ",z)
    
    
  