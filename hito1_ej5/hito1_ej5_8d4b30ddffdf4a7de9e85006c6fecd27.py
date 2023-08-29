#Cálculo del dígito verificador de un rut
rut = int(input())
n7 = (rut % 10) * 2
n6 = ((rut // 10) % 10) * 3
n5 = ((rut // 100) % 10) * 4
n4 = ((rut // 1000) % 10) * 5
n3 = ((rut // 10000) % 10) * 6
n2 = ((rut // 100000) % 10) * 7
n1 = ((rut // 1000000) % 10) * 2
n0 = (rut // 10000000) * 3
sum = n7 + n6 + n5 + n4 + n3 + n2 + n1 + n0
resto = sum % 11
i = 11 - resto
if i == 11:
    print ("dv=0")
elif i == 10:
    print ("dv=K")
else:
    print ("dv=",i)
