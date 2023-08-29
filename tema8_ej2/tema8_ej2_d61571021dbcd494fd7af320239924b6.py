def buscarTodas(a,b):
    a = [str(x) for x in a]
    find = []
    for x,y in enumerate(a):
        if y == b:
            find.append(x)
            print(find)
    Pal = ' '.join([str(y) for y in find])
    return(Pal)

if __name__ == "__main__":
    pass
           