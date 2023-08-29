def subsecuencia(secuencia,n):
    largo = len(secuencia)
    g = 0
    i = 0
    while g<largo-n:
        string = secuencia[g:n+g]
        g = g + 1
        if string in secuencia[n:]:
            pass
        else:
            print(string)
            i=+1
    if i == 0:
        print("ninguna")
print(subsecuencia(secuencia=input("secuencia:"),n=int(input("n:"))))      