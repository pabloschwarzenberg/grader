def buscarTodas(a, b):
    list = []
    for i in range(len(a)):
        if a[i] in b:
            list.append(str(i))
    return " ".join(list)


if __name__ == "__main__":
    pass
           