#Descomponer un número
numero = int(input('Escribe un numero de 4 digitos: '))
mi = numero//1000
ce = numero//100%10
de = numero%100//10
un = numero%10
if 1 <= numero <= 9999:
    print(mi, 'M +', ce, 'C +', de, 'D +', un, 'U')
else:
    print('Numero mal escrito')
         