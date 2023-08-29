def numero_perfecto(a):
    i = 1
    numero = a
    suma = 0
    while i < numero:
        if numero%i == 0:
            suma = suma+i
        i = i+1
    if suma == numero:
       return True
    else:
       return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           