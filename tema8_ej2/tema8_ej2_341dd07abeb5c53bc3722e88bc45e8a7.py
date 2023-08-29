def buscarTodas(a, b):
    aa = [i for i, x in enumerate(a) if x == b]
    bb = list(aa)
    cc = []
    for i in bb:
        cc.append(str(i))
    string = " ".join(cc)
    return string

if __name__ == "__main__":
    pass
           