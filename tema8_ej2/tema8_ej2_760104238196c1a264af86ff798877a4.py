def buscarTodas(a, b):
    lsta = []
    for i in range(len(a)):
        if a[i] == b:
            lsta.append(str(i))
            lsta.append(' ')
    return ''.join(lsta[:-1])
    


if __name__ == "__main__":
    pass
