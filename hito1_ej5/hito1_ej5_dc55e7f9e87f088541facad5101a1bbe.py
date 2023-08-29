rut = int(input('Ingresa tu rut sin dígito verificador: '))

# 1° Tomar los dígitos del RUT por separado, de derecha a izquierda.

d1 = rut%10   # Con %10 Conseguimos el último dígito
rut = rut//10  # Con //10 le sacamos al rut el último dígito. Se sobreescribe rut.

d2 = rut%10
rut = rut//10

d3 = rut%10
rut = rut//10

d4 = rut%10
rut = rut//10

d5 = rut%10
rut = rut//10

d6 = rut%10
rut = rut//10

d7 = rut%10
rut = rut//10

d8 = rut%10
rut = rut//10

print(d1, d2, d3, d4, d5, d6, d7, d8)

d1 = d1*2
d2 = d2*3
d3 = d3*4
d4 = d4*5
d5 = d5*6
d6 = d6*7
d7 = d7*2
d8 = d8*3
suma=d1+d2+d3+d4+d5+d6+d7+d8
div=suma%11
dv=11-div
if dv==11:
    dv=0
if dv==10:
    dv='k'
print("dv=",dv)