def numero_perfecto(a):
    s = 0
    for i in range(1, a):
        if a%i == 0:
            s += i

    return s == a

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           