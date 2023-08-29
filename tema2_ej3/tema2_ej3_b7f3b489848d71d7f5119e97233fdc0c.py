def numero_perfecto(a):
    Sumaaas = 0
    for p in range(1, a):
        r = a % p
        if r == 0:
            Sumaaas = Sumaaas + p
    if Sumaaas == a:
      return 1
    else:
      return 0