#Cálculo del dígito verificador de un rut
print('** VERIFICADOR DE RUT **')

rut = int(input())
verif = 89456789
verif1 = 9456789
rut_s = str(rut)
verif_s = str(verif)
verif1_s = str(verif1)

lista_rut = []
lista_ver = []

if len(rut_s) == 8:
    cont = 0
    while cont < len(rut_s):
        lista_rut.append(rut_s[cont])
        lista_ver.append(verif_s[cont])
        cont = cont + 1

    lista_nueva = []
    n = 0
    while n < len(rut_s):
        mult = int(lista_rut[n])*int(lista_ver[n])
        lista_nueva.append(mult)
        n = n+1

    suma = 0
    for i in lista_nueva:
        suma = suma + i

    digito = suma%11
    if digito == 10:
        print('dv=k')
    else:
        print('dv='+str(digito))

if len(rut_s) == 7:
    cont = 0
    while cont < len(rut_s):
        lista_rut.append(rut_s[cont])
        lista_ver.append(verif1_s[cont])
        cont = cont + 1

    lista_nueva = []
    n = 0
    while n < len(rut_s):
        mult = int(lista_rut[n])*int(lista_ver[n])
        lista_nueva.append(mult)
        n = n+1

    suma = 0
    for i in lista_nueva:
        suma = suma + i

    digito = suma%11
    if digito == 10:
        print('dv=k')
    else:
        print('dv='+str(digito))
