def numero_perfecto(a):

    lista = []
    for i in range(1, a):
        residuo = a % i
        if residuo == 0:
            lista.append(i)
        else:
            continue
    
    suma = sum(lista)

    if suma == a:
        return True
    
    else:
        return False

if __name__ == "__main__":
    print(numero_perfecto(int(input("Valor: "))))