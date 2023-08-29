def buscarTodas(a, b):
    indices = []
    pos = 0
    while True:
        pos = a.find(b, pos)
        if pos == -1:
            break
        indices.append(str(pos))
        pos += 1
    return ' '.join(indices)

if __name__ == "__main__":
    a = 'tres tristes tigres'
    b = 't'
    print(buscarTodas(a, b)) # debería imprimir '0 5 9 13'
