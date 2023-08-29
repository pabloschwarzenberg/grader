def ocultar_letras(palabra,cantidad):
    from random import choice
    a=palabra
    a = list(a)
    c=1
    p=100
    while c <= cantidad:
        b = a.index(choice(a))
        if b!=p:
            p=b
            c+=1
            for l,i in enumerate(a):
                if l == b:
                    a[b] = "_"
        else:
            continue
    palabra = "".join(a)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    z = list(palabra_secreta)
    x = list(palabra)
    print(z)
    print(x)
    for n,b in enumerate(palabra_secreta):
        print(n,b)
        if letra == b:
            x[n] = b
    palabra = "".join(x)
    return palabra
if __name__ == "__main__":
    pass
         