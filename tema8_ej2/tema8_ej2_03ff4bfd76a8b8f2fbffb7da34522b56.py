def buscarTodas(a, b):
    indices = []
    i = 0
    while i < len(a):
        if a[i:i+len(b)] == b:
            indices.append(str(i))
            i += len(b)
        else:
            i += 1
    return ' '.join(indices)
if __name__ == "__main__":
    # Ejemplo de uso
    a = 'tres tristes tigres'
    b = 't'
    print(buscarTodas(a, b))
