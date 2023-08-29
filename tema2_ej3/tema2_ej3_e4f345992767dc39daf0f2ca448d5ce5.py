def numero_perfecto(n):
    ds = []
    for i in range(1, n):
        if n%i == 0:
            i = ds.append(i)
    
    ##sumar divisores
    s = 0
    for d in ds:
        s = s + d
    if s == n:
        ep = True
    else:
        ep = False
    return ep
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a)) 
           