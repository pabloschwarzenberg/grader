def buscarTodas(a,b):
    string = ''
    for i in range(0,len(a)):
        if b == a[i] and i < 1:
            string += str(i)
        elif b == a[i]:
            string = string + ' ' + str(i)
        else:
            continue
    return string

if __name__ == "__main__":
    palabra = input('ingrese frase')
    letra = input('ingrese letra')
    print(buscarTodas(palabra,letra))
    pass
           