def DescomponerUnNumero():
    numero=input('Ingrese un numero mayor que cero y menir que 9999: ')
    PruebaLogica=len(numero)<5

    if PruebaLogica==True:
        Numero=numero
        numero=numero.zfill(4)
        numero=((numero.replace('','-')).split('-'))
        del numero[0]
        del numero[len(numero)-1]
        numero.reverse()
        u,d,c,m='{}U'.format(numero[0]),'{}D'.format(numero[1]),'{}C'.format(numero[2]),'{}M'.format(numero[3])
        print('{} :\t{}+{}+{}+{}'.format(Numero,m,c,d,u))

    else:
        print('Intentemoslo otra vez, bueno?\n')
        return DescomponerUnNumero()

DescomponerUnNumero()


numeroso='0124'