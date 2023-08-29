def numero_perfecto(a):
    perfecto = 0
    for i in range(1, a):
        if a % i == 0:
            perfecto = perfecto + i
    num_perfecto = False
    if a == perfecto:
        num_perfecto = True
    else:
        False
    return(num_perfecto)
    

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           