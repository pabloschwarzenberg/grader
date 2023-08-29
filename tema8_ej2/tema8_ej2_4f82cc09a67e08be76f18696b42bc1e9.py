def buscarTodas(a,b):
    indices = []
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            indices.append(str(i))
    return ' '.join(indices)

if __name__ == "__main__":
    a = 'tres tristes tigres'
    b = 't'
    print(buscarTodas(a,b)) # debería imprimir "0 5 9 13"