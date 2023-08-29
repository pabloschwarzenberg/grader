def buscarTodas(a,b):
    L=[]
    for i in range(len(a)):
        if a[i]==b:
            L.append(str(i))
    return " ".join(L)

if __name__ == "__main__":
    pass
           