#Contestador de celular
n = str(input('ingrese numero telefonico: '))
h = int(input('ingrese hora de la llamda: '))

if h >= 0 and h <= 7:
    print('Contestar')
elif h < 14:
    if n.endswith('909'):
        print('Contestar')
    else:
        print('No constear')
        
elif h >= 17 and h <= 19:
    if n.startswith('877'):
        print('No contestar')
    else:
        print('Contestar')
else:
    print('No contestar')
    
