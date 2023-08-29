#Cálculo del dígito verificador de un rut

r = input()
l = len(r)
r = r[::-1]
r = r
i = 0
m = 2
a = 0

while i < l:
    if m > 7:
        m = 2
    a += (int(r[i]) * m)
    i += 1
    m += 1

a = a % 11
a = 11 - a
if a == 11:
    dv = 0
elif a == 10:
    dv = 'k'
else:
    dv = a

print('dv =', dv)
