def buscarTodas(a,b):
    search = ''
    for i in range(0,len(a)):
        if b == a[i]:
            search += str(i)
            search += ' '
    searchf = search[:-1]
    return searchf
    pass

if __name__ == "__main__":
    a = input()
    b = input()
    print(buscarTodas(a,b))
    pass
           