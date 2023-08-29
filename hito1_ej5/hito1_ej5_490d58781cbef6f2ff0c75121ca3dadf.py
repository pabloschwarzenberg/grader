X=int(input())
a=X//10000000
b=(X//1000000)%10
c=(X//100000)%10
d=(X//10000)%10
e=(X//1000)%10
f=(X//100)%10
g=(X//10)%10
h=X%10
SP=2*h+3*g+4*f+5*e+6*d+7*c+2*b+3*a
W=SP%11
V=11-W
if V==11:
  print("dv=",0)
if V==10:
    print("dv=k")
else:
    print("dv=",V)
      