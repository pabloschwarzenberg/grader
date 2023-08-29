def buscarTodas(a, b):
    indices = []
    pos = 0
    while pos < len(a):
        index = a.find(b, pos)
        if index != -1:
            indices.append(str(index))
            pos = index + 1
        else:
            break
    return ' '.join(indices)

if _name_ == "_main_":
    a = input("Ingrese la cadena a: ")
    b = input("Ingrese la subcadena b: ")
    resultado = buscarTodas(a, b)
    print("Índices encontrados:", resultado)
    resultado = buscarTodas(a, b)
    print("Índices encontrados:", resultado)