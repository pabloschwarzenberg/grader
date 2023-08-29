def se(a,b,c,d,e,f):
    ecc= a*e - b*d
    if ecc != 0:
        x = (c*e - b*f)/ecc
        y = (a*f - c*d)/ecc
        print('x=',x)
        print('y=',y)
    else:
        print('Sin solución.')


a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

print(se(a,b,c,d,e,f))