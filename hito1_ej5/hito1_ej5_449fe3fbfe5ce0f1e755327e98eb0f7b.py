#Cálculo del dígito verificador de un rut
rut = input('Ingresa tu RUT sin puntos y sin el dígito verificador: ')
dig = list(rut)
print(dig)
dig.reverse() 
print(dig)

for n in range(len(dig)):
    dig[n] = int(dig[n])
print(dig)

for i in range(len(dig)):
    if i<6:
        dig[i] = dig[i]*(i+2)
    else:
        dig[i] = dig[i]*(i-4)
print(dig)

suma = 0
for a in range(len(dig)):
    suma = suma+dig[a]
print(suma)
print(suma%11)
r = 11-(suma%11)
print(r)

if r==11:
    print('dv=0')
elif r==10:
    print('dv=K')
else:
    print('dv=',r)