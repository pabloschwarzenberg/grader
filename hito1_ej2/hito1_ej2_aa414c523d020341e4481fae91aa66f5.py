#Contestador de celular
n1 = str(input('Ingrese numero telefónico: '))
n2 = int(input('Ingrese hora de llamada: '))

if len(str(n1)) == 8:
    if n2 > 0 and n2 <= 7:
        print('Resultado: Contestar')
    if (n2 > 7 and n2 <= 14) and n1[5:] == '909':
        print('Resultado: Contestar')
    if n1[5:] != '909':
        print('Resultado: No Contestar')
    if (n2 > 14 and n2 < 17 ):
        print('Resultado: No Contestar')
    if n2 > 17 and n2 < 19 :
        if n1[:4] == '877':
            print('Resultado: No contestar')
        if not(n1[:4] == '877'):
            print('Resultado: Contestar')
    elif n2 > 19:
        print('Resultado: No contestar ')