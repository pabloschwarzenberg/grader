#Cálculo del dígito verificador de un rut
rut = int(input('ingresa un rut: '))
D1 = (rut // 1) % 10
D2 = (rut // 10) % 10
D3 = (rut // 100) % 10
D4 = (rut // 1000) % 10 
D5 = (rut // 10000) % 10 
D6 = (rut // 100000) % 10
D7 = (rut // 1000000) % 10
D8 = (rut // 10000000) % 10

p1 = D1*2
p2 = D2*3
p3 = D3*4
p4 = D4*5
p5 = D5*6
p6 = D6*7
p7 = D7*2
p8 = D8*3

suma = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8

resto = suma % 11
verificador = 11 - resto

if verificador == 10:
    print('dv = k')
elif resto == 0:
    print('dv = 0')
else:
    print('dv ='+str(verificador))
