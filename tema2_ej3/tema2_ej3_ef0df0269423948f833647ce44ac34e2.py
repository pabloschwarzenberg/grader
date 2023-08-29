def numero_perfecto(a):
    suma = 0

    x = a 
    while (x > 0):
        if (a%x == 0):
            if x != a:
                suma = suma + x
        x = x - 1
    
    if suma == a: 
        return True
    
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           