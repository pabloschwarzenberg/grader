def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
        if numero%i==1:
          return True
        else:
        return False