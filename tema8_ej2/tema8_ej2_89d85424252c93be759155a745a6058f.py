def buscarTodas(a,b):
    result = ''
    for l in range(len(a)):
        if b == a[l]:
            result = result + str(l) + ' '
    return result.strip()