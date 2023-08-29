def buscarTodas(a, b):
    s = ''
    for i in range(len(a)):
        if a[i] == b:
            s += str(i) + ' '
    if len(s) == 0:
        print('no existe')
    print(s[0:-1])