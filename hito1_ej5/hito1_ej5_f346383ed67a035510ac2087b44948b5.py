#Cálculo del dígito verificador de un rut
a = str(input('ingrese su rut sin numero identificador: '))
a1 = []
for i in range(len(a)):
    a1.append(a[i])
    
a1.reverse()
a2=[int(i) for i in a1]
          
e = [2, 3, 4, 5, 6, 7, 2, 3]
o = []

for i in range(len(a2)):
    o.append(a2[i]*e[i])
u = sum(o)

u1 = u/11
u1 = int(u1)
u1 = u1*11
u2 = u-u1
u2 = 11-u2

if u2 == 10:
    print('dv=k')
elif u2 == 11:
    print('dv=0')
else:
    print('dv=',u2)