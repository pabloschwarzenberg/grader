#Contestador de celular

def contestar():
    x = int(input('Ingrese numero telefonico: '))
    x1 = str(x)
    y = int(input('Ingrese hora de la llamada: '))
    if y<7 or y < 14 and x1[5:] == '909': 
        print('CONTESTAR')
    elif 17 < y < 19 and x1[0:3] != '877':
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
contestar()