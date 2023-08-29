def buscarTodas(a,b):
    pos = []
    i = 0
    while i < len(a):
        if a[i] == b:
            pos.append(str(i))
        i += 1
    return ' '.join(pos)

if __name__ == "__main__":
    palabra = input("Palabra:")
    letra = input("Letra: ")
    resp = buscarTodas(palabra,letra)
    print(resp)