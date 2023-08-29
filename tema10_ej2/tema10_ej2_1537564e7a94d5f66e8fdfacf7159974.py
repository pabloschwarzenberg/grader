def distancia(pal_1,pal_2):
    if pal_1 == pal_2:
        res = '0D'
    elif len(pal_1) == len(pal_2):
        contador=0
        for i in range(len(pal_1)):
            if pal_1[ i ] != pal_2[ i ]:
                contador += 1
            if contador == 1:
                res = '1S'
            else: res = '+1'
    else:
        if len(pal_1) < len(pal_2):
            larga = pal_2
            corta = pal_1
        else:
            larga = pal_1
            corta = pal_2
        inside = False
        for i in range(len(larga)):
            dentro = (corta == ( larga[ 0:i ] + larga[ i+1:len(larga) ] ))
            inside = inside or dentro
        if inside: res = 'IB'
        else: res = '+1'
    return res

if __name__ == "__main__":
    pal_1 = input('Palabra 1? ').strip()
    pal_2 = input('Palabra 2? ').strip()
    a=distancia(pal_1,pal_2)
    print(a)
