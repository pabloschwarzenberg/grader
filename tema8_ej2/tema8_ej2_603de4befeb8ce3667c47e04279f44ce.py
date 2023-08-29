def buscarTodas(a,b):
    n = list(a)
    cord = []
    c = 0
    for i in n:
        if i == b:
            cord.append(str(c))
        c = c + 1     
    cord_n = str(" ".join(cord))
    return cord_n
if __name__ == "__main__":
    pass
           