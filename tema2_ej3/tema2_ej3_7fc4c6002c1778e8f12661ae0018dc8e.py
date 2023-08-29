def numero_perfecto(a):
    suma = 0
    for i in range(1,a+1):
        if a % i == 0 :
            suma += i
            #print(suma)
            if suma - a == a:
                return True
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
