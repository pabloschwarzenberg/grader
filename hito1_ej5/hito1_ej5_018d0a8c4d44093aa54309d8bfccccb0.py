#Cálculo del dígito verificador de un rut
x= int(input())
a= x//10000000
b= (x-a*10000000)//1000000
c= (x-(a*10+b)*1000000)//100000
d= (x-(a*100+b*10+c)*100000)//10000
e= (x-(a*1000+b*100+c*10+d)*10000)//1000
f= (x-(a*10000+b*1000+c*100+d*10+e)*1000)//100
g= (x-(a*100000+b*10000+c*1000+d*100+e*10+f)*100)//10
h= (x-(a*1000000+b*100000+c*10000+d*1000+e*100+f*10+g)*10)//1

y=h*2+g*3+f*4+e*5+d*6+c*7+2*b+3*a
w= y//11
z= y-w*11
t= 11-z
if t==11:
    print("dv=0")
elif t==10:
     print("dv=k")
else:
     print("dv="+str(t)+"")