def buscarTodas(a, b):
    little_list = []
    for i in range(len(a)):
        if a[i] == b:
            little_list.append(str(i))
    big_list = " ".join(little_list)
    return (big_list)