a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

det = a * e - b * d
x = (e * c - b * f) / det
y = (a * f - d * c) / det

print("x=",x)
print("y=",y)