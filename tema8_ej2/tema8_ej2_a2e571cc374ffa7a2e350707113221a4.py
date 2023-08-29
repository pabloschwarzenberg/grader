def buscarTodas(a, b):
    a_list = []
    indices = []
    conta = 0
    contb = 0
    while conta < len(a):
        a_list.append(a[conta])
        conta += 1
    while contb < len(a_list):
        if a_list[contb] == b:
            indices.append(contb)
        contb += 1
    indices = " ".join(str(x) for x in indices)
    return indices


if __name__ == "__main__":
    pass
           