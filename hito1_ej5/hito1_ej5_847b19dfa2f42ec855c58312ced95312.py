n=int(input())
a=(n%10)
b=(((n%100)-(n%10))/10)
c=(((n%1000)-(n%100))/100)
d=(((n%10000)-(n%1000))/1000)
e=(((n%100000)-(n%10000))/10000)
f=(((n%1000000)-(n%100000))/100000)
g=(((n%10000000)-(n%1000000))/1000000)
h=(((n%100000000)-(n%10000000))/10000000)
i=(2*a)
j=(3*b)
k=(4*c)
l=(5*d)
m=(6*e)
n=(7*f)
o=(2*g)
p=(3*h)
suma= (i+j+k+l+m+n+o+p)
mod = (suma//11)
otro= (suma - (11*mod))
fin= (11-otro)
if (fin ==11):
    print("dv=0")
elif (fin ==10):
    print("dv=k")
else:
    print("dv=",fin)