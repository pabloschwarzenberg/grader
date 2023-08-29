# completa el código de la función
def suma_divisores(a):
    a = abs(a)
    if a == 1:    #Caso Base
        return 1
    if a > 1:     #Caso recursivo
        suma = a + sumaDivisores(a%(a-1))
        return suma
print(sumaDivisores(2))
  return
           