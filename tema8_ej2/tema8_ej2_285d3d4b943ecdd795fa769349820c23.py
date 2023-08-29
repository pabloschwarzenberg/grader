def buscarTodas(a,b):
    bt = []
    pl =" "
    for i in range(len(a)):
        if (a[i]==b):
            bt.append(str(i))
            pp = pl.join(bt)
    return pp

if __name__ == "__main__":
    pass
           