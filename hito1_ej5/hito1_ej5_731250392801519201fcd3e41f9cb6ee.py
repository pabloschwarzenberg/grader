
n=int(input())
a= n//10000000
b= n//1000000 - a*10
c= n//100000 -(a*100 + b*10)
d= n//10000 -(a*1000 + b*100 + c*10)
e= n//1000 -(a*10000 + b*1000 + c*100 + d*10)
f= n//100 -(a*100000 + b*10000 + c*1000 + d*100 + e*10)
g= n//10-(a*1000000 + b*100000 + c*10000 + d*1000 + e*100 + f*10)
h= n -(a*10000000 + b*1000000 + c*100000 + d*10000 + e*1000 + f*100 + g*10)

print(a , b , c , d , e , f , g , h )

h2= h*2
g2= g*3
f2= f*4
e2= e*5
d2= d*6
c2= c*7
b2= b*2
a2= a*3

s= (a2 + b2+ c2+ d2+ e2+ f2+ g2 + h2)%11 
dv= 11 - s

if dv == 10:
   print("dv=k ")
elif dv == 11:
     print("dv=0")
else:
     print("dv=", dv)