'''Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.'''
print('El programa permite ingresar 3 numeros ENTEROS\n y los mostrara en orden ascendente...')
NumA,NumB,NumC=eval(input('\nIngrese un numero entero:\t')),eval(input('\nIngrese otro numero entero:\t')),eval(input('\nIngrese un ultimo numero entero:\t'))
#print(NumA, NumB, NumC)
cond1=NumA<=NumB<=NumC
msj1='Los numeros de Menor a mayor son:\t{}, {}, {}'.format(NumA, NumB, NumC)
#print(msj1)
cond2=NumA<=NumC<=NumB
msj2='Los numeros de Menor a mayor son:\t{}, {}, {}'.format(NumA, NumC, NumB)
cond3=NumB<=NumA<=NumC
msj3='Los numeros de Menor a mayor son:\t{}, {}, {}'.format(NumB, NumA, NumC)
cond4=NumB<=NumC<=NumA
msj4='Los numeros de Menor a mayor son:\t{}, {}, {}'.format(NumB, NumC, NumA)
cond5=NumC<=NumA<=NumB
msj5='Los numeros de Menor a mayor son:\t{}, {}, {}'.format(NumC, NumA, NumB)
cond6=NumC<=NumB<=NumA
msj6='Los numeros de Menor a mayor son:\t{}, {}, {}'.format(NumC, NumB, NumA)

PruebaLogica = type(NumA)==type(NumB)==type(NumC)==int
#print(PruebaLogica)

if cond1 and PruebaLogica:
    print(msj1)
elif cond2 and PruebaLogica:
    print(msj2)
elif cond3 and PruebaLogica:
    print(msj3)
elif cond4 and PruebaLogica:
    print(msj4)
elif cond5 and PruebaLogica:
    print(msj5)
elif cond6 and PruebaLogica:
    print(msj6)
else:
    print('\nNumeros invalidos.\n')
print('\n\t\t--FIN--')