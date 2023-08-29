b=float(input("a: "))
c=float(input("b: "))
a=float(input("c: "))
e=float(input("d: "))
f=float(input("e: "))
d=float(input("f: "))
Y1=b*d-e*a
Y2=b*f-e*c
Y=Y1/Y2
X1=a-c*((b*d-e*a)/(b*f-e*c))
X2=b
X=X1/X2
round(Y,1)
round(X,1)
print("x=",X,"Y=",Y)      