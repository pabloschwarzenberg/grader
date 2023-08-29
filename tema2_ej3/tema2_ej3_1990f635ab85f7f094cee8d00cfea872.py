def numero_perfecto(a):
    inicio = 0
    for i in range(1,a):
        if a % i == 0:
            inicio += i
    if inicio == a:
        return True
    else:
        return False
if __name__=="__main__":
    a = int(input("Ingrese un numero: "))
    if __name__=="__main__":
        print(numero_perfecto(a))
           