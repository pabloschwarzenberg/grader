def buscarTodas(a,b):
    c = ''
    for i in range(len(a)):
        if b in a[i]:
            if c != '':
                c += ' ' + str(i)
            
            else:
                c += str(i)
    return c
           