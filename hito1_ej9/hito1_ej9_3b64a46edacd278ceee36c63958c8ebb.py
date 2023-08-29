x1 = int(input(""))
y1 = int(input(""))
r1 = int(input(""))
x2 = int(input(""))
y2 = int(input(""))
r2 = int(input(""))

y3 = y1*x2-y2*x1
r3 = r1*x2-r2*x1
Y = r3/y3
X = (r1-y1*Y)/x1

Y = round(Y,1)
X = round(X,1)

print("X=",X)
print("Y=",Y)
