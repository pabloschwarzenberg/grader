def buscarTodas(a,b):
    pocicion=""
    i=0
    while i<len(a):

        if a[i]==b:
            i=str(i)
            pocicion+= " " + i
            i=int(i)
            i+=1
        else:
            i+=1

    return pocicion[1:]

if __name__ == "__main__":
    pass
           