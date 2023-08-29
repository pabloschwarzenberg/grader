#Cálculo del dígito verificador de un rut
rut = eval(input('Ingresa tu rut sin puntos:'))
print('\n')

n1 = rut%10
n2 = (rut%100)//10
n3 = (rut%1000)//100
n4 = (rut%10000)//1000
n5 = (rut%100000)//10000
n6 = (rut%1000000)//100000
n7 = (rut%10000000)//1000000
n8 = rut//10000000

m1 = n1 * 2
m2 = n2 * 3
m3 = n3 * 4
m4 = n4 * 5 
m5 = n5 * 6
m6 = n6 * 7
m7 = n7 * 2
m8 = n8 * 3

mt = m1+m2+m3+m4+m5+m6+m7+m8
mtr = mt%11
dgt = 11 - mtr
if dgt==11:
    print('dv=0')
elif dgt==10:
    print('dv=k')
else:
    print('dv=',dgt)