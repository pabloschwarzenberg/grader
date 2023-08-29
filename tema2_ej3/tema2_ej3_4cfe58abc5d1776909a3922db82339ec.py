def numero_perfecto(a):
  suma_divisores = 0
  contador = 1
  perfecto = False

  while contador < a:
    if (a % contador) == 0:
      suma_divisores = suma_divisores + contador
    contador = contador + 1 

  if suma_divisores == a:
    perfecto = True

  return perfecto