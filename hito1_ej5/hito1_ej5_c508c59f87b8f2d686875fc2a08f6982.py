rut=int(input())
a= rut//10000000
b= (rut-a*10000000)//1000000
c= (rut-a*10000000-b*1000000)//100000
d= (rut-a*10000000-b*1000000-c*100000)//10000
e= (rut-a*10000000-b*1000000-c*100000-d*10000)//1000
f= (rut-a*10000000-b*1000000-c*100000-d*10000-e*1000)//100
g= (rut-a*10000000-b*1000000-c*100000-d*10000-e*1000-f*100)//10
h= (rut-a*10000000-b*1000000-c*100000-d*10000-e*1000-f*100-g*10)//1
h= h*2
g= g*3
f= f*4
e= e*5
d= d*6
c= c*7
b= b*2
a= a*3
suma=a+b+c+d+e+f+g+h
entera=suma//11
resto=suma-(11*entera)
v=11-resto
if v==11:
    v=0
elif v==10:
    v="K"
else:
    v==v
print("dv=",v)