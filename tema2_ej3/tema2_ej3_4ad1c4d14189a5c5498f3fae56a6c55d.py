def numero_perfecto(a):
    lista_divisores = []
    for i in range(1,a):
        if a%i == 0:
            lista_divisores.append(i)
    suma = 0
    for i in lista_divisores:
        suma += i
    if suma == a:
        return True
    else:
        return False

if __name__=="__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
