def suma_divisores(a):
    divis = []
    for div in range(1,a):
        if (a%div) == 0:
            divis.append(div)
    if divis == [1]:
        primo = True
        return (sum(divis), primo)
    elif divis != [1]:
        primo = False
        return (sum(divis), primo)