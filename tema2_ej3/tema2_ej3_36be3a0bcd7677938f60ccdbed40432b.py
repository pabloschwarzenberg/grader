def numero_perfecto(a):
    b = 0
    i = 1
    while i < a:
        if a%i == 0:
            b = b+i
        i = i+1
    if b == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           