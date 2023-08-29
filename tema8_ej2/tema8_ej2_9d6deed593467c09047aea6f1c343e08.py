def buscarTodas(a,b):
    indices = []
    for i in range(len(a)):
        if a[i] == b:
            indices.append(str(i))
    return ' '.join(indices)
    pass

if __name__ == "__main__":
    a = 'tres tristes tigres'
    b = 't'
    print(buscarTodas(a,b))






    pass
           