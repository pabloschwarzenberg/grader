def buscarTodas(a, b):
    string = ''
    for i in range(len(a)):
        if b in a[i]:
            string += str(i)+' '
    return string.strip(' ')        