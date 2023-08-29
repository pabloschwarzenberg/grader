#Ordenar tres números
a=int(input()) 
b=int(input()) 
c=int(input())
if c<=b<=a:
    print("{},{},{}".format(c,b,a))
elif b<=c<=a:
    print("{},{},{}".format(b,c,a))
elif c<=a<=b:   
    print("{},{},{}".format(c,a,b))
elif a<=c<=b:
    print("{},{},{}".format(a,c,b))
elif b<=a<=c:
    print("{},{},{}".format(b,a,c))
else:  #a<=b<=c
    print("{},{},{}".format(a,b,c))

