def ExtraerNumeros(nrorut):
    if len(nrorut) == 8:
        a = int(rut[0])
        b = int(rut[1])
        c = int(rut[2])
        d = int(rut[3])
        e = int(rut[4])
        f = int(rut[5])
        g = int(rut[6])
        h = int(rut[7])

    else:
        str(nrorut)
        nuevorut = '0' + nrorut
        a = int(nuevorut[0])
        b = int(nuevorut[1])
        c = int(nuevorut[2])
        d = int(nuevorut[3])
        e = int(nuevorut[4])
        f = int(nuevorut[5])
        g = int(nuevorut[6])
        h = int(nuevorut[7])

    digv = (h * 2) + (g * 3) + (f * 4) + (e * 5) + (d * 6) + (c * 7) + (b * 2) + (a * 3)
    digv1 = digv / 11
    digv2 = str(digv1)
    digv3 = digv2[0:2]
    digv4 = int(digv3)
    digv5 = digv - (11 * digv4)
    digv6 = 11 - digv5

    if digv6 == 11:
        print('dv=0')
    elif digv6 == 10:
        print('dv=K')
    else:
        print('dv=', digv6)


##########


rut = input('Ingrese rut sin puntos ni guion: ')
ExtraerNumeros(rut)
