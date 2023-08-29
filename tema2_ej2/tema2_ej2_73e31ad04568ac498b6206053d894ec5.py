# completa el código de la función
def obtener_divisores(numero):
  
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def amigos(a,b):
    divisores_a = obtener_divisores(a)
    divisores_b = obtener_divisores(b)
    
    suma_divisores_a = sum(divisores_a)
    suma_divisores_b = sum(divisores_b)
    
    return suma_divisores_a == b and suma_divisores_b == a
           