def buscarTodas(a,b):
    var =[idx for idx, x in enumerate(a) if x==b]
    c=var[len(var)-1]
    el_espacio = ''
    for i in var:
        if i !=c:
            el_espacio = el_espacio + str(i) + ' '
        else:
            el_espacio = el_espacio + str(i)
    return el_espacio

if __name__ == '__main__':
    pass
           