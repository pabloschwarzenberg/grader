#Cálculo del dígito verificador de un rut
rut = input()
multi = [2,3,4,5,6,7,2,3,4,5,6,7]
suma = 0
for i in range(len(rut)):
    suma += int(rut[-i-1])*multi[i]

ver = 11 - (suma%11)
if ver == 11:
    ver = 0
elif ver == 10:
    ver = 'K'

print('dv=',ver)      