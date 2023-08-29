def numero_perfecto(a):
    adicion = 0
    for l in range(1, a):
        if (a % l == 0):
            adicion += l

    if a == adicion:
        return True
    else:
        return False

    if numero_perfecto(a):
        return True
    else:
        return False 
    

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           