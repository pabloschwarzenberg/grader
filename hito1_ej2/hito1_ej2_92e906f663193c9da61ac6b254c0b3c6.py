#Contestador de celular
while True:
    n = int(input('Ingrese un número telefónico: '))
    if (len(str(n))>8) or (len(str(n))<8):
        print('El número marcado no existe: ')
        continue
    else:
        h = int(input('Ingrese la hora de la llamada: '))
        if (h>23) or (h<0):
            print('Ingrese una hora válida')
            continue
        else:
            break
nl = list(str(n))
d = [nl[5],nl[6],nl[7]]
f = ['9','0','9']
b = [nl[0],nl[1],nl[2]]
f1 = ['8','7','7']
if h>19:
    print('NO CONTESTAR')
elif h in range(0, 7):
    print('CONTESTAR')
elif h in range(0,14) or d==f:
    print('CONTESTAR')
elif h in range(17, 19) and b!=f1:
    print('CONTESTAR')
else:
    print('NO CONTESTAR')
      