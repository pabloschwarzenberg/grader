def buscarTodas(a,b):
    a = list(a)
    print(a)
    a = [index for (index, item) in enumerate(a) if item == b]
    print(a)
    for i in range(len(a)):
        a[i] = str(a[i])
    a = " ".join(a)
    return a

if __name__ == "__main__":
    palabra = input()
    letra= input()
    print(buscarTodas(palabra, letra))
           