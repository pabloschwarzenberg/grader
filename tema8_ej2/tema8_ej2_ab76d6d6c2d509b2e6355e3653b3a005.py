def buscarTodas(a, b):
    indices = []
    start = 0
    while start < len(a):
        index = a.find(b, start)
        if index == -1:
            break
        indices.append(str(index))
        start = index + 1
    return ' '.join(indices)


if __name__ == "__main__":
    a = 'tres tristes tigres'
    b = 't'
    result = buscarTodas(a, b)
    print(result)
