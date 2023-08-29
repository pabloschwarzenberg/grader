# completa el código de la función
def amigos(numero):
    suma = 0
    
    for i in range(1,numero):
        if numero%1 == 0:
            suma += 1
    return suma

a = int(input("Ingrese primer numero:"))
b = int(input("ingrese segundo numero:"))
    
if amigos(a) == b and amigos(b) == a: 
    return True
else:
  return False
