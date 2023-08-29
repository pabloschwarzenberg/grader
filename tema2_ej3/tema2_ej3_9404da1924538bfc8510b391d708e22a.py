def numero_perfecto(a):
    suma = 0
    i = 1
    while i < a:
        if a % i == 0:
            suma += i
        i += 1
    if suma == a:
      return True
    else:
      return False         