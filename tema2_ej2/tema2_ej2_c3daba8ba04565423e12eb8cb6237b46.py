def amigos(a, b):
    resultado = []
    n = 1
    while n < a:
        if a % n == 0:
            resultado.append(n) 
        n = n + 1
    return resultado 
if __name__ == "__main__":
  a = int(input("Ingrese número 1: "))
  b = int(input("Ingrese número 2: "))
  d = amigos(a, b)
  c = sum(d)

  if c == b:
      print("True")
  else:
      print("False")