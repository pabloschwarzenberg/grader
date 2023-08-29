a = int(input(" "))
b = int(input(" "))
c = int(input(" "))

if a>=b>=c:
    print(c,",",b,",",a)
elif b>=a>=c:
    print(c,",",a,",",b)
elif c>=a>=b:
    print(b,",",a,",",c)
elif c>=b>=a:
    print(a,",",b,",",c)

