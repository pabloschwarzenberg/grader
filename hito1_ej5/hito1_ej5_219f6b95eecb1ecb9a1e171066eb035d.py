#Cálculo del dígito verificador de un rut
rut_sin_dv = int(input("RUT sin dígito verificador: "))
rut_str = str(rut_sin_dv)
rut_lista = []
for digito in rut_str:
    rut_lista.append(int(digito))
rut_lista.reverse()
lista_mult = [2,3,4,5,6,7,2,3,4,5,6,7]
suma=0
n=0
while n<=len(rut_lista)-1:
    mult = rut_lista[n]*lista_mult[n]
    suma+=mult
    n+=1
resto=suma%11
d_v_=11-resto
dv=0
if d_v_==11:
    dv=0
elif d_v_==10:
    dv=str(dv)
    dv='K'
else:
    dv=d_v_
print("dv=",dv)