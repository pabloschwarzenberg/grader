def numero_perfecto(n):
    D_I = []
    for i in range(1, n):
        if n%i == 0:
            i = D_I.append(i)
    
    SUMA = 0
    for div in D_I:
        SUMA = SUMA + div
    if SUMA == n:
        esPerfecto = True
    else:
        esPerfecto = False
    return esPerfecto
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           