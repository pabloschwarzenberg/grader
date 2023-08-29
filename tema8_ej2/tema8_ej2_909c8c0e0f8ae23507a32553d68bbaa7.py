def buscarTodas(a,b):
    c=list(a)
    d = [i for i, x in enumerate(c) if x == b]
    e = [str(k) for k in d]
    f = " ".join(e)
    return f

if __name__ == "__main__":
    pass
           