#Cálculo del dígito verificador de un rut
numero = input('Ingrese el número:')
#numero = int(input('Ingrese parte numerica del RUT:'))
largo = len(numero)
contador=1
sumador = 0
for i in range(largo-1,-1,-1): #[0,1,2,3,4,5,6,7]
    contador = contador+1
    sumador= sumador + int(numero[i])*contador
    if contador==7:
        contador=1
#print(sumador)
resto = sumador%11
#print(resto)

DV = 11 - resto
#print(dv)
DV=str(DV)
if DV =='11':
   DV = '0'
if DV =='10':
   DV ='K'
print('dv=',DV)      