def suma_divisores(num):
    suma = 0
    for ez in range(1, num):
        if num % ez == 0:
            suma += ez
    return suma
  if num == suma:
    return True
  else:
    return False