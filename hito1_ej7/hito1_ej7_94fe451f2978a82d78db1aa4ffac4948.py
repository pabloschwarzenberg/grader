#Zodiaco

dia = int(input('\nDía de Nacimiento: '))
mes = int(input('Mes de Nacimiento: '))

if mes==1:
    if dia<20:
        print('\nCapricornio')
    elif dia>=20:
        print('\nAcuario')
elif mes==2:
    if dia<19:
        print('\nAcuario')
    elif dia>=19:
        print('\nPiscis')
elif mes==3:
    if dia<21:
        print('\nPiscis')
    elif dia>=21:
        print('\nAries')
elif mes==4:
    if dia<20:
        print('\nAries')
    elif dia>=20:
        print('\nTauro')
elif mes==5:
    if dia<21:
        print('\nTauro')
    elif dia>=21:
        print('\nGeminis')
elif mes==6:
    if dia<21:
        print('\nGeminis')
    elif dia>=21:
        print('\nCancer')
elif mes==7:
    if dia<23:
        print('\nCancer')
    elif dia>=23:
        print('\nLeo')
elif mes==8:
    if dia<23:
        print('\nLeo')
    elif dia>=23:
        print('\nVirgo')
elif mes==9:
    if dia<23:
        print('\nVirgo')
    elif dia>=23:
        print('\nLibra')
elif mes==10:
    if dia<23:
        print('\nLibra')
    elif dia>=23:
        print('\nEscorpio')
elif mes==11:
    if dia<22:
        print('\nEscorpio')
    elif dia>=22:
        print('\nSagitario')
elif mes==12:
    if dia<22:
        print('\nEscorpio')
    elif dia>=22:
        print('\nSagitario')