def numero_perfecto(a):
    divi = [1]

    for i in range(2, a + 1):
        if a % i == 0:
            divi.append(i)
    divi.remove(a)

    if sum(divi) == a:
        Perfecto = True
        return (Perfecto)
    else:
        Perfecto = False
        return(Perfecto)