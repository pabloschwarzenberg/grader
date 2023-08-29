def solucion(a,b,c,d,e,f):
    deter= a*e-b*d
    if deter!=0:
        x=(c*e-b*f)/deter
        y=(a*f-c*d)/deter
        return print("x=",x),print ("y=",y)

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
(solucion(a,b,c,d,e,f))