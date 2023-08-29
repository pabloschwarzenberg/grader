def numero_perfecto(a):
    div = []
    for i in range(1, a+1):
        if a%i == 0:
            if i != a:
                div.append(i)
    suma = sum(div)
    print(div)
    if suma == a:
        return True
    elif suma != a:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           