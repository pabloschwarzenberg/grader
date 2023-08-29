def suma_divisores(a):
    suma = 0
    y = True
    if a <=1:
        y = False
    elif a == 2 :
        y = True
    else:
        for i in range(2, a):
            if a % i == 0:
                y = False

    return (suma,y)
      