def numero_perfecto(x):
    suma = 0
    for z in range(1,x):
      if x%z == 0:
        suma = suma + z
    if suma == x:
      return True
    else:
      return False