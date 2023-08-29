def buscarTodas(a,b):
    posiciones = ''

    i = 0
    while i < len(a):
        if a[i] == b:
            posiciones += str(i) + ' '
        i+= 1
    
    return posiciones[:-1]

if __name__ == "__main__":
    pass
           