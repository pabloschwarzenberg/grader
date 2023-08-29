#Cálculo del dígito verificador de un rut
RUT = input('ingrese rut: ')
L = len(RUT)
n = '23456723'
S = 0


while L > 0:
    S += (int(RUT[L-1]))*(int(n[0]))
    RUT = RUT[:L-1]
    n = n[1:]
    L = len(RUT)
S %= 11
dv = 11 - S
if dv == 10:
    print('dv= K')
elif dv == 11:
    print('dv= 0')
else:
    print('dv=',dv)     