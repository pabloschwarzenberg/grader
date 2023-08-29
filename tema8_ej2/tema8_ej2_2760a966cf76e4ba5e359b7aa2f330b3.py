def buscarTodas(a,b):
    fran = ""
    for i in range(0,len(a)):
        if a[i] == b and i < len(a):
            fran += str(i) + " "
    fran = fran.strip(" ")
    return fran

if __name__ == "__main__":
    pass
           