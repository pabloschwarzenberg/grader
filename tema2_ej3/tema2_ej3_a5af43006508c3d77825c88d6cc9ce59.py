def numero_perfecto(a):
    b = []
    for i in range(1,a):
        if a%i == 0:
            b.append(i)
    if sum(b) == a:    
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))