rut = eval(input('Ingrese rut (8 digitos):' ))
n1 = (rut % 10)
n2 = (rut // 10) % 10
n3 = (rut // 100) % 10
n4 = (rut // 1000) % 10
n5 = (rut // 10000) % 10
n6 = (rut // 100000) % 10
n7 = (rut // 1000000) % 10
n8 = (rut // 10000000) % 10
#print(n1 , n2, n3, n4, n5, n6, n7, n8)
r1 = n1 * 2
r2 = n2 * 3
r3 = n3 * 4
r4 = n4 * 5
r5 = n5 * 6
r6 = n6 * 7
r7 = n7 * 2
r8 = n8 * 3
s = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8
#print(s)
de = s // 11
#print(de)
rde = s - (11 * de)
#print(rde)
resultado = 11 - rde
#print(resultado)
if resultado == 11:
    print('dv=0')
elif resultado == 10:
    print('dv=K')
else:
    resultado = 'dv=' + str(resultado)
    print(resultado)