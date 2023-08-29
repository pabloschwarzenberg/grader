rut = int(input())

a = rut%10
b = (rut//10)%10
c = (rut//100)%10
d = (rut//1000)%10
e = (rut//10000)%10
f = (rut//100000)%10
g = (rut//1000000)%10
h = (rut//10000000)%10

summ = a*2+b*3+c*4+d*5+e*6+f*7+g*2+h*3
x=summ/11
y=int(x)

r=11-(summ-(11*y))
if r == 11:
    print("dv=0")
elif r == 10:
    print("dv=k")
else:
    print("dv=",r)      