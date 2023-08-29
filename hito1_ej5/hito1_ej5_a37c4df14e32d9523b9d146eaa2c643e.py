#Cálculo del dígito verificador de un rut
rut=input('Ingrese rut:\t')
rut=((rut.replace('', '-')).split('-'))
del rut[0]
del rut[(len(rut)-1)]
rut.reverse()
valores=[2,3,4,5,6,7]
dvp1=int()
dv=int()
pEntera=int()
resta=int()
parcial=int()

for i in range(len(rut)):
        parcial=int(rut[i])*valores[i%6]
        dvp1=dvp1+parcial

pEntera=dvp1//11
resta=(dvp1-(11*pEntera))
dv=11-resta

if dv==11:
    dvp=0
elif dv==10:
    dvp='k'
else:
    dvp=dv
print('dv={}'.format(dvp))      