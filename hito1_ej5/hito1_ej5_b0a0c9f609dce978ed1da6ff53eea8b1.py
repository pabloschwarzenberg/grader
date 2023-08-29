rut = input()
rut_reverso = rut[::-1]
mult = 2
suma = 0
for num in rut_reverso:
    suma = suma + (int(num) * mult)
    if mult < 7:
        mult += 1
    else:
        mult = 2
dv = 11 - (suma - (int(suma/11) * 11))
if dv == 11:
    dv = 0
elif dv == 10:
    dv = 'K'
print("dv="+ str(dv))
