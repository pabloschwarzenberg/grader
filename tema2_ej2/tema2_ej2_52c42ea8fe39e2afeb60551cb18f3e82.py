def amigos(num1, num2):

  def obtenerSumaDivisores(numero):
    suma = 0
    for i in range(1, numero-1):
        if numero % i == 0:
            suma += i
    return suma
 
  if obtenerSumaDivisores(num1) == num2 and obtenerSumaDivisores(num2) == num1:
    return True
  else:
    return False