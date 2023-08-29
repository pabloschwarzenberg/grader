def suma_divisores(a):

    lista = []    # Aqui guardaremos los divisores de "a".
    for i in range(1, a):
        residuo = a % i
        if residuo == 0:
            lista.append(i)
        else:
            continue

    suma = sum(lista)
    
    if suma == 1:
        return suma, True
    else:
        return suma, False

if __name__ ==  "__main__":
    print(suma_divisores(int(input("Valor: "))))