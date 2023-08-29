#Cálculo del dígito verificador de un rut
rut = int(input("ingrese su rut sin el numero digitador: "))
a=rut//10**7 
b = rut%10**7 
c=b//10**6 
d = b%10**6 
e=d//10**5 
f = d%10**5 
g=f//10**4 
h = f%10**4 
i=h//10**3 
j = h%10**3 
k=j//10**2 
l = j%10**2 
hi=l//10**1 
o = l%10**1 
p=o//10**0 
q = p * 2
r = hi * 3
s = k * 4
t = i * 5
u = g * 6
v = e * 7
w = c * 2
x = a * 3
y = q+r+s+t+u+v+w+x
z = y//11
na = y-(11*z)
ja = 11-na
if ja == 11:
    print("dv","=",0)
elif ja == 10:
    print("dv","=","K")
else:
    print("dv","=",ja)