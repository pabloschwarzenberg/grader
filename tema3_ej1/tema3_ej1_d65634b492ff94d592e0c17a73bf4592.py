def sumaDivisores(n):
  def encontrarDivisores(m):
    if m > 0:
      if n%m == 0:
        arr.append(m)
      encontrarDivisores(m-1)
  arr = []
  encontrarDivisores(n)
  print("El número %d, tiene %s divisores; Suman %d." % (n, arr, sum(arr)))