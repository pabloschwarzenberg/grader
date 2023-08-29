def decodificar(mensaje):
    mensaje = list(mensaje)
    for i in range(len(mensaje)):
        if mensaje[i] ==',':
            mensaje.pop(i)
            mensaje.append('')
    n = 8
    lista = []
    for i in range(len(mensaje)):
        k = mensaje[8*i:8*(i+1)]
        k = "".join(k)
        k = str(k)
        if k =='01100001':
             lista.append('a')
        elif k == '01100010':
             lista.append('b')
        elif k == '01100011':
             lista.append('c')
        elif k == '01100100':
             lista.append('d')
        elif k == '01100101':
             lista.append('e')
        elif k == '01100110':
             lista.append('f')
        elif k == '01100111':
             lista.append('g')
        elif k == '01101000':
             lista.append('h')
        elif k == '01101100':
             lista.append('l')
        elif k == '01101101':
             lista.append('m')
        elif k == '01101110':
             lista.append('n')
        elif k == '01101111':
             lista.append('o')
        elif k == '01110000':
             lista.append('p')
        elif k == '01110001':
             lista.append('q')
        elif k == '01110010':
             lista.append('r')
        elif k == '01110011':
             lista.append('s')
        elif k == '01110100':
             lista.append('t')
        elif k == '01110101':
             lista.append('u')
        elif k == '01110110':
             lista.append('v')
        elif k == '01110111':
             lista.append('w')
        elif k == '01111000':
             lista.append('x')
        elif k == '01111001':
             lista.append('y')
        elif k == '01111010':
             lista.append('z')
    l = "".join(lista)
    
    return (l)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         