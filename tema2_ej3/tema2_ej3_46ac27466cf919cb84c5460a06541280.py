def numero_perfecto(a):
    suma = 0
    for i in range(1,a + 1):
        b = a/i
        c = a//i
        if c == a:
            continue
        elif b == float(c):
            suma += c
    if suma == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    pass
           