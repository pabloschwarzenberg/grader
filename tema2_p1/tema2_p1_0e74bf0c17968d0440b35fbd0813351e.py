# por favor escribe aquí tu función
def es_primo(numero):
  return
  
  #Ingreso de datos y operacion

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

#Respuesta
print(es_primo(7))  
print(es_primo(10))  
print(es_primo(23))

           