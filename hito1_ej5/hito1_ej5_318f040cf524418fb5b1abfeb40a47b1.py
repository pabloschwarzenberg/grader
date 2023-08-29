#Cálculo del dígito verificador de un rut
rut = int(input())
lista = []
for i in str(rut):
    lista.append(i)
lista.reverse()
multiplo = 2
dv = 0
for i in lista:
    dv += int(i)*multiplo
    if multiplo == 7:
        multiplo = 2
    else:
        multiplo += 1
dv = 11-(dv % 11)

if dv == 11:
    dv = 0
elif dv == 10:
    dv = 'k'

print('dv=',end='')
print(dv)
