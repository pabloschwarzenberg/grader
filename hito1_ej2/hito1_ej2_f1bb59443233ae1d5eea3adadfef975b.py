numero= []
numero.append(input('Ingrese numero telefonico: '))
numero.append(input('ingrese hora de la llamda: '))
celular = numero[0]
hora= int(numero[1])

if hora>= 0 and hora<= 7:
    print('contestar')

if hora> 7 and hora< 14:
    if int(celular[-3:]) == 909:
        print('contestar')
    else:
        print('no contestar')

if hora>= 17 and hora<= 19:
    if int(celular[0:3]) == 877:
        print('no contestar')
    else:
        print('contestar')

if hora> 19 and hora<= 23:
    print('no contestar')
