def numero_perfecto(a):
    resultado=[]
    for n in range(1,a-1):
        if a%n == 0:
            resultado.append(n)
    if sum(resultado)==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
