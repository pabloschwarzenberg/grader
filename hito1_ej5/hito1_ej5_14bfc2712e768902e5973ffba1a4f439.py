#Cálculo del dígito verificador de un rut
print('Ingrese su rut sin puntos ni digito verificador   ')
rut=input()
lista_rut=[]
lista_digitos=[2,3,4,5,6,7,2,3,4,5,6]
suma=0
for f in range(len(rut)):
    lista_rut.append(rut[f])
    
lista_rut_1=list(reversed(lista_rut))
lista_rut_1=[int(x) for x in lista_rut_1]
for f in range (len(lista_rut_1)):
    a=(int((lista_rut_1)[f]))*(int((lista_digitos)[f]))
    suma=suma+a

z=suma%11
y=11-z
if y<=9 and y>=1:
    print('dv=',y)
elif y==11:
    print('dv=0')
elif y==10:
    print('dv=K')
