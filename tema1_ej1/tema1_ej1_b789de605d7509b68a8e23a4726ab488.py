'''La suma de los primeros n numeros naturales está dada por n(n + 1)/2.
Crea un programa que reciba como parámetro un número N y luego imprima la suma de los N primeros números naturales'''
print('Suma de los N primeros números naturales\n\n\n')
NumNat=eval(input('Ingrese un número:\t\t'))
#print(type(NumNat))
PruebaLogica=type(NumNat)==int
if PruebaLogica is True:
    SumNumNat=(NumNat*(NumNat+1)/2)
    print('La suma de los primeros {} números naturales es:\t{}'.format(NumNat, SumNumNat))
else:
    print('Numero Inadecuado')
print('--FIN--')