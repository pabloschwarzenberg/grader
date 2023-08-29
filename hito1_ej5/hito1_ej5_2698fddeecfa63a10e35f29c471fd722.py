#Cálculo del dígito verificador de un rut
rut = input('Ingrese su rut: ')
largo = len(rut)
i = largo - 1 
x = 2         
sumador = 0
while i > -1:
    digito = rut[i]
    valor = int(digito) * x
    sumador += valor
    i -= 1 
    x += 1
    if x == 8:
        x = 2
dv = sumador%11
dv = 11-dv
if dv == 11:
    dv = 0
elif dv == 10:
    dv = 'k'
print('DV =',str(dv))     