def numero_perfecto(a):
    divi = []
    
    for i in range(1, a):
        if a%i == 0:
            divi.append(i)
    b = sum(divi)
    
    if (a - b) == 0:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           