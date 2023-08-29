def numero_perfecto(n):
  lista = []
  for i in range(n + 1):
    if i != n and i != 0 and n % i == 0:
      lista.append(i)
  if sum(lista) == n:
    return(True)
  else:
    return(False)

if __name__=="__main__":
  n=int(input("Ingrese n: "))
  print(numero_perfecto(n))
           