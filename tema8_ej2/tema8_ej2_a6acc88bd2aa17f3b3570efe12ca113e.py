def buscarTodas(a,b):
    l=[]
    for x in range(len(a)):
        if a[x]==b:
            l.append(str(x))
    return " ".join(l)

if __name__ == "__main__":
    pass
           