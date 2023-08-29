#Cálculo del dígito verificador de un rut
rut = (input('Ingrese el rut: '))
largoRut = len(str(rut))
ListaRut = list(rut)
print(ListaRut)
if largoRut == 8:
    n8 = int(ListaRut[7]) * 2
    n7 = int(ListaRut[6]) * 3
    n6 = int(ListaRut[5]) * 4
    n5 = int(ListaRut[4]) * 5
    n4 = int(ListaRut[3]) * 6
    n3 = int(ListaRut[2]) * 7
    n2 = int(ListaRut[1]) * 2
    n1 = int(ListaRut[0]) * 3
    Total = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
    dv = Total % 11
    Final = 11 - dv
    if Final == 11:
        Final = '0'
    elif Final == 10:
        Final = 'K'

elif largoRut == 7:
    n7 = int(ListaRut[6]) * 2
    n6 = int(ListaRut[5]) * 3
    n5 = int(ListaRut[4]) * 4
    n4 = int(ListaRut[3]) * 5
    n3 = int(ListaRut[2]) * 6
    n2 = int(ListaRut[1]) * 7
    n1 = int(ListaRut[0]) * 2
    Total = n1 + n2 + n3 + n4 + n5 + n6 + n7 
    dv = Total % 11
    Final = 11 - dv
    if Final == 11:
        Final = '0'
    elif Final == 10:
        Final = 'K'
print('dv = ' + str(Final))