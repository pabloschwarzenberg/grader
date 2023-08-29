def numero_perfecto(num):
  lista = []
  for x in range(num + 1):
    if x != num and x != 0 and num % x == 0:
      lista.append(x)
  if sum(lista) == num:
    return(True)
  else:
    return(False)

if __name__=="__main__":
    num=int(input("Ingrese un número: "))
    print(numero_perfecto(num))