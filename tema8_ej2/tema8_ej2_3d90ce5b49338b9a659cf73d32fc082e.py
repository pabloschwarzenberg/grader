def buscarTodas(a, b):
    new = ""
    for i in range(len(a)):
        if a[i] == b:

            new += str(i)
            new += " "
    return new.rstrip()