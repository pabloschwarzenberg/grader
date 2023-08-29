def numero_perfecto(a):
    valor=range(1,a)
    divisores=0
    for n in valor:
        if a % n == 0:
            divisores+=n
    if divisores==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           