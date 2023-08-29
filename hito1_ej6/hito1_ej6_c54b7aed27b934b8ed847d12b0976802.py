a=int(input("ingrese un numero: "))
b=int(input("ingrese un segundo numero: "))
c=int(input("ingrese un tercer numero: "))

def mayor(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    elif c>=a and c>=b:
        return c

def minor(a,b,c):
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    elif c<=a and c<=b:
        return c
def middle(a,b,c):
    if (a<=b and a>=c)or(a>=b and a<=c):
        return a
    elif (b<=a and b>=c)or(b>=a and b<=c):
        return b
    elif (c<=b and c>=a)or(c>=b and c<=a):
        return c
p=minor(a,b,c)
s=middle(a,b,c)
t=mayor(a,b,c)
    
print(str(p)+","+str(s)+","+str(t))



      