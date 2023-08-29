def suma_divisores(a):
    div=[1]

    for x in range(2,a+1):
        if a % x == 0:
            div.append(x)

    borrar = div.index(a)
    del div[borrar]

    if sum(div)==1:
        return ( (sum(div)), True )
    else:
        return ( (sum(div)), False )         