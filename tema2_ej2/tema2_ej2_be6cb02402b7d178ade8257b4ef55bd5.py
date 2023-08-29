# completa el código de la función
def amigos(a,b):
    numero_a = 0
    numero_b = 0
    for i in range(1, a):
        if a % i == 0:
            numero_a = numero_a + i
    for i in range(1, b):
        if b % i == 0:
            numero_b = numero_b + i
    return numero_a == b and numero_b == a

    if numero_a == b and numero_b == a:
        return True
    else:
        return False

a = 220
b = 284
print(amigos(a,b))
            
 
           