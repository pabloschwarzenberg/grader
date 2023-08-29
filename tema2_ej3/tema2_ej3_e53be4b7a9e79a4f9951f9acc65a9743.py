def numero_perfecto(a):
    Lista_divisores = []
    for i in range(1, a):
        if a % i == 0:
            Lista_divisores.append(i)
    sumadiv = int(sum(Lista_divisores))
    if sumadiv == a:
        return True
    return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           