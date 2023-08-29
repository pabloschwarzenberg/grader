def amigos(l,h):
    suma1 = 0
    for i in range(1,l):
        if l%i == 0:
            suma1 += i

    suma2 = 0
    for i in range(1,h):
        if h%i == 0:
            suma2 += i
    print(suma2)

    if suma1 == h and suma2 == l:
      amigos = True
    else:
      amigos = False

    return(amigos)