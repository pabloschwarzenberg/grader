rut=input()
aux=2
suma=0
for i in range(len(rut)):
    a=int(rut[len(rut)-(i+1)])*aux
    aux=aux+1
    if aux==8:
        aux=2
    suma=suma+a
    print(a)
print(suma)
resto=suma%11
resultado=11-resto
if resultado==10:
  resultado='k'
if resultado==11:
  resultado=0
print('dv=',resultado)