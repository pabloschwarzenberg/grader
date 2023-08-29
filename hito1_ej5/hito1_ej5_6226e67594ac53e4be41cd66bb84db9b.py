#7 rut

rut = input('Ingrese el numero de su rut (sin guion ni digito verificador):')
inverso = rut[::-1]
x= 2
s = 0

for i in inverso:
    s+= int(i) * x
    x += 1
    if x == 8:
        x = 2

r= s % 11
v = 11 - r

if v == 11:
    v = 0
elif v == 10:
    v = 'K'

print('dv='+str(v))