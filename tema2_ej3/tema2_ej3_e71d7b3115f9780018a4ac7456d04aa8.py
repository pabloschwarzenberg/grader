def numero_perfecto(a):
    divisores = []
    sumax = 0
    for x in range(1,a):
        divisor = a/x
        if divisor == int(divisor):
            divisores.append(x)
            sumax = sumax+x
    if sumax == a :
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           