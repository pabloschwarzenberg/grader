def numero_perfecto(a):
  lista = []
  for i in range(1,a):
    divisor = a%i
    if divisor == 0:
      lista.append(i)

  if sum(lista) == a:
    return True

  else:
    return False
           