def buscarTodas(a, x):
    b = ""
    i = 0
    c = 0
    while i < len(a):
        if a.find(x) != -1:
            if b != "":
                b += " "
            c = str(a.find(x))
            b += c
            a = a.replace(x, "<", 1)
        i += 1
    return b