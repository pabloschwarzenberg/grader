def subsecuencias (secuencia, n):
    dic = {}

    for a in range(len(secuencia) - (n - 1)):
        if secuencia[a:n] in dic:
            dic[secuencia[a:n]] += 1
        else:
            dic[secuencia[a:n]] = 1
        n += 1
    
    contador = 0
    for n in dic:
        if dic[n] > 1:
            pass
        elif dic[n] == 1:
            contador += 1
            print(n)
    if contador > 0:
        pass
    elif contador == 0:
        print("ninguna")


secuencia = input()
n = int(input())
subsecuencias(secuencia, n)