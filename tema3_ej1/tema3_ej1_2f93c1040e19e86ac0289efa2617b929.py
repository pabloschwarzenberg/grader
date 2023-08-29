# completa el código de la función
def suma_divisores(a):
    div =[]
    for i in range(1, a):
        if a % i == 0:
            div.append(i)
    div=sum(div)
    if div == 1:
        return div, True
    else:
        return div, False
    return 
if __name__ == "__main__":
    a = int(input("ingrese el numero deseado: "))
    resultado=suma_divisores(a)
    print(resultado)
           