
def lol(numero, hora):
    if hora >= 0 and hora < 7:
        return 'CONTESTAR'
    elif hora < 14:
        return 'CONTESTAR'
    elif hora <= 13 and str(numero)[-3:-4] =='909':
      return 'CONTESTAR'
    elif hora >= 17 and hora < 19 and not str(numero).startswith('877'):
        return 'CONTESTAR'
    else:
        return 'NO CONTESTAR'

n= input('Ingrese numero telefonico:')
h= int(input('Ingrese hora de la llamada:'))

r = lol(n, h)
print(r)