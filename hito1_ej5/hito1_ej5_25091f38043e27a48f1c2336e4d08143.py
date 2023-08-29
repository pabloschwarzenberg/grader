#Cálculo del dígito verificador de un rut
R=int(input("rut"))
a=(R//10000000)
fa=a*3
b=(R//1000000)-(a*10)
fb=b*2
c=(R//100000)-(a*100)-(b*10)
fc=c*7
d=(R//10000)-(a*1000)-(b*100)-(c*10)
fd=d*6
e=(R//1000)-(a*10000)-(b*1000)-(c*100)-(d*10)
fe=e*5
f=(R//100)-(a*100000)-(b*10000)-(c*1000)-(d*100)-(e*10)
ff=f*4
g=(R//10)-(a*1000000)-(b*100000)-(c*10000)-(d*1000)-(e*100)-(f*10)
fg=g*3
h=R-(a*10000000)-(b*1000000)-(c*100000)-(d*10000)-(e*1000)-(f*100)-(g*10)
fh=h*2
S=fa+fb+fc+fd+fe+ff+fg+fh
D=S%11
dv=11-D
if dv>10:
    print("dv="+str(0))
elif dv==10:
    print("dv=k")
else:
    print("dv= "+str(dv))
      