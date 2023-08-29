def buscarTodas(a,b):
    i = 0
    n = 0
    l = len(a)
    indices = []
    while n < l:
        i = str(a.find(b,n,l))
        print(i)
        print((indices.count(i)))
        if indices.count(i) == 0:
            indices.append(str(i))
        n += 1
    indices.remove('-1')
    indices = ' '.join(indices)
    return indices


if __name__ == "__main__":
     a = input('Ingrese un string: ')
     b = input('Ingrese la letra que quiere buscar: ')
     print(buscarTodas(a,b))

           