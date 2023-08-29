a = int(input(''))
b = int(input(''))
c = int(input(''))
d = int(input(''))
e = int(input(''))
f = int(input(''))

x = (b*f-e*c)/(b*d-a*e)
y = (a*f-c*d)/(a*e-b*d)

print('x='+str(round(x, 1)))
print('y='+str(round(y, 1)))