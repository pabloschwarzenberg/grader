def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    fila = []
    for line in archivo:
        a = line.splitlines()
        b = ''.join(a)
        b = b.lower()
        c = b.split(' ')
        fila += [c]
    archivo.close()
    y = []
    m = ''
    for a in fila[0]:
        m += a
        if m in palabras:
            y += [(palabras[palabras.index(m)], [0, 0], 'derecha')]
    i = 0
    j = 0
    m = ''
    while i <= 2 and j <= 3:
        m += fila[i][j]
        i += 1
        if m in palabras:
            y += [(palabras[palabras.index(m)], [0, 1], 'abajo')]
        if i == 3:
            j += 1
            i = 0
            m = ''
    m = ''
    m += fila[0][0]
    m += fila[1][1]
    m += fila[2][2]
    if m in palabras:
        y += [(palabras[palabras.index(m)], [0, 0], 'diagonal')]
    return y



if __name__=="__main__":
  print(sopaletras('sopa.txt', ['casa']))
  print(sopaletras('sopa.txt', ['cra']))
  print(sopaletras('sopa.txt', ['aro']))
