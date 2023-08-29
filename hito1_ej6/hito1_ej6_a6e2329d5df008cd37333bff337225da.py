#Ordenar tres números
a = int(input())
b = int(input())
c = int(input())

d = str(a)
e = str(b)
f = str(c)

if a>=b and a>=c:
    if b>=c:
        print(f+","+e+","+d)
    else:
        print(e+","+f+","+d)
elif b>=a and b>=c:
    if a>=c:
        print(f+","+d+","+e)
    else:
        print(d+","+f+","+e)
else:
    if a>=b:
        print(e+","+d+","+f)
    else:
        print(d+","+e+","+f)