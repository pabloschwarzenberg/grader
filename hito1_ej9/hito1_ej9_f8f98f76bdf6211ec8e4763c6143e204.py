a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

# A + B = C
# D + E = F

delta = (a * e) - (d * b)

delta_x = (c * e) - (f * b)
delta_y = (a * f) - (d * c)

x = delta_x / delta
y = delta_y / delta

print("x=" + str(x))
print("y=" + str(y))  