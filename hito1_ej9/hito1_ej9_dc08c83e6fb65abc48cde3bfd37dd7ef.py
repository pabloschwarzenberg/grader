a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
x=(b*f-e*c)/(b*d-a*e)
y=(a*f-d*c)/(-d*b+a*e)
x=round(x,1)
y=round(y,1)
z="['x={}',y={}']".format(x,y)
print(z)


    