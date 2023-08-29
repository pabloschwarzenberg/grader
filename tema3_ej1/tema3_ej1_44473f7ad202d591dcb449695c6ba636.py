def suma_divisores(a):
    divi = [1]
    

    for i in range(2, a + 1):
        if a % i == 0:
            divi.append(i)
    divi.remove(a)

    if sum(divi) == 1:
        primo = True
        return (sum(divi), primo)
    else:
        primo = False
        return(sum(divi), primo)
