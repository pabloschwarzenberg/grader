def son_amigos(numero1, numero2):
    def sumar_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma
    
    suma1 = sumar_divisores(numero1)
    suma2 = sumar_divisores(numero2)
    
    if suma1 == numero2 and suma2 == numero1:
        return True
    else:
        return False
