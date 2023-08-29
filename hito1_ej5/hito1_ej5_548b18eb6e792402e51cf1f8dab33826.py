#Cálculo del dígito verificador de un rut
rut = eval(input("Ingrese su RUT sin dígito verificador: "))

#19812159

d1 = rut // 10000000
d2 = (rut // 1000000) % 10
d3 = (rut // 100000) % 10
d4 = (rut // 10000) % 10
d5 = (rut // 1000) % 10
d6 = (rut // 100) % 10
d7 = (rut // 10) % 10
d8 = rut % 10

op1 = d8*2 + d7*3 + d6*4 + d5*5 + d4*6 + d3*7 + d2*2 + d1*3

op2 = op1 // 11

op3 = op1 - (11*op2)

op4 = 11-op3

if op4 >= 11:
    print("dv=0")
elif op4 == 10:
    print("dv=k")
else:
    print("dv=",op4)