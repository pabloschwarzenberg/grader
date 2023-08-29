a = int(input())
b = int(input())
c = int(input())

if a>=b and b>=c:
    print("{},{},{}".format(c,b,a))
elif a>=c and c>=b:
    print("{},{},{}".format(b,c,a))
elif b>=a and a>=c:
    print("{},{},{}".format(c,a,b))
elif b>=c and c>=a:
    print("{},{},{}".format(a,c,b))
elif c>=a and a>=b:
    print("{},{},{}".format(b,a,c
                            ))
else:
    print("{},{},{}".format(a,b,c))
    

