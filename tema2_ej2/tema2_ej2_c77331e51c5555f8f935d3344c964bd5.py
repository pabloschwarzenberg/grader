def amigos(a,b):
    resultado=[]
    for n in range(1,a-1):
        if a%n == 0:
            resultado.append(n)
    if sum(resultado)==b:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    b=int(input("Ingrese b: "))
    print(amigos(a,b))

