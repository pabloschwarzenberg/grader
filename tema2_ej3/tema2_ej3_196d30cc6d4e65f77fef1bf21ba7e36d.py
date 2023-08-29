def numero_perfecto(a):
    Suma = 0
    for p in range(1, a):
        R = a % p
        if R == 0:
            Suma = Suma + p
    if Suma == a:
      return 1
    else:
      return 0