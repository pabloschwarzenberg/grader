def amigos(a, b):
    def suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma
    
    return suma_divisores(a) == b and suma_divisores(b) == a
print(amigos(220, 284)) # amigos
print(amigos(1184, 1210)) # no amigos 
print(amigos(220, 281)) # no amigos


    

