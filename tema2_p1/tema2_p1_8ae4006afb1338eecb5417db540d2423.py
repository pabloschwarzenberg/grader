# por favor escribe aquí tu función
def es_primo(num):
 if num < 2: #si es menor de 2 no es primo, devolverá Falso
   return False
 for i in range(2, num): #un ciclo desde el 2 hasta el num de entrada
   if num % i == 0: #si el resto da 0 no es primo, devuelve Falso
    return False
 return True #de lo contrario devuelve Verdadero