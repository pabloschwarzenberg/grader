#Contestador de celular

num = int(input('Digite el numero telefonico: '))
hora = int(input('Digite la hora de la llamada: '))

while hora <= 23 and hora >= 0:
    if hora < 14:
        if hora >= 0 and hora <= 7:
            print('CONTESTAR')
            break
        if int(str(num)[-3:]) == 909:
            print('CONTESTAR')
            break
        else:
            print('NO CONTESTAR')
            break

    elif hora >= 14 and hora <= 19:
        if hora >= 17 and hora <= 19:
            if int(str(num)[:3]) == 877:
                print('NO CONTESTAR')
                break
            else:
                print('CONTESTAR')
                break
        else:
            print('NO CONTESTAR')
            break

    else:
        print('NO CONTESTAR')
        break