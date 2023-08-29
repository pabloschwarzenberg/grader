def suma_divisores(a):
    suma=0
    valor=1
    while valor<a:
        if a%valor==0:
            suma+=valor
        valor +=1
    if a<2:
        return suma,False
    for i in range(2,a):
        if a%i==0:
            return suma,False
    return suma,True
 
if __name__ == "__main__":
    for i in [1,8,13]:
        s = suma_divisores(i)
        print(s)
