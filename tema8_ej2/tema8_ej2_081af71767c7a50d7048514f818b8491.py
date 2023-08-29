def buscarTodas(a,b):
    i = 0
    cadena = ''
    while i < len(a):
        #print('len',len(a))
        if b == a[i]:
            cadena = cadena + str(i) + ' ' 
            print('cadena', cadena)
        i = i+1
        #print('i',i)
    cadena = cadena[:-1]
    return cadena           