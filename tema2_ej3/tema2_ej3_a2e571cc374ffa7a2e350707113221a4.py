def numero_perfecto(a):
    cont = 0
    suma = 0
    while cont < a:
        try:
            if a%cont == 0:
                suma += cont
        except ZeroDivisionError:
            pass
        cont+= 1
    if suma == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           