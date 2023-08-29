def numero_perfecto(a):
    count = 1
    divs = []
    while count < a:
        if a % count == 0:
            divs.append(count)
        count += 1
    if sum(divs) == a:
        return True
    else:
        return False