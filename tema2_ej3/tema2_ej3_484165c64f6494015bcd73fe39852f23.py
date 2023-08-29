def numero_perfecto(a):
  lista = []
  for x in range(a + 1):
    if x != a and x != 0 and a % x == 0:
      lista.append(x)
  if sum(lista) == a:
    return(True)
  else:
    return(False)

  if _name=="main_":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           