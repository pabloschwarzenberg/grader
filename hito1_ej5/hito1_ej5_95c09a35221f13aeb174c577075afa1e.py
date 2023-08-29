a=int(input())

b=(a%10)
c=(a%100)
d=int(c/10)
e=(a%1000)
f=int(e/100)
g=(a%10000)
h=int(g/1000)
i=(a%100000)
j=int(i/10000)
z=(a%1000000)
l=int(z/100000)
m=(a%10000000)
n=int(m/1000000)
ñ=(a%100000000)
o=int(ñ/10000000)

p=((b*2)+(d*3)+(f*4)+(h*5)+(j*6)+(l*7)+(n*2)+(o*3))
q=(p%11)
r=(11-q)

if r == 10:
    print("dv=k")

elif r == 11:
    print("dv=",0)

else:
    print("dv=",r)