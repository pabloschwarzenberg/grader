def suma_divisores(a):
    count = 1
    divs = []
    while count < a:
        if a % count == 0:
            divs.append(count)
        count += 1
    if sum(divs) == 1:
        prime = True
    else:
        prime = False
    return sum(divs), prime


