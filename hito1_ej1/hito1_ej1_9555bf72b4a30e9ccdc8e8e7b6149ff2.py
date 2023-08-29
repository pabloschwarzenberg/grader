PT=float(input())
PI=float(input())
NE=float(input())
PP=float(input())

x=PT*3+PI*3+NE*3+PP
a=2*(x-int(x))          #Define redondeo

if a>=1:
    x=int(x+1)
    print(x/10)
else:
    x=int(x)
    print(x/10)