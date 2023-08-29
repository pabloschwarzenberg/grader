def numero_perfecto(a):
    i = a - 1
    suma = 0
    while i > 0 :
        if a%i == 0 :
            suma = suma + i
            i = i - 1
        else:
            i = i - 1
            
    if suma == a :
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           