# por favor escribe aquí tu función
def es_primo(num):
  #si es menos que 2 no es primo, por lo tanto devolverá Falso
  if num < 2:
    return False
    #un rango desde el dos hasta el numero que nosotros elijamos
  for i in range(2, num):
    #si el resto da 0 no es primo, por lo tanto devuelve Falso
    if num % i == 0:
      return False
  #de lo contrario devuelve Verdadero
  return True
#para probarlo llamamos a la función
           