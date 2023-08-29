def suma_divisores(a):

  def encontdivisor(b):

    if b > 0:

      if a%b == 0:

        ar.append(b)

      encontdivisor(b-1)

  ar = []

  encontdivisor(a)

  print("El número %d, tiene %s divisores; suman %d." % (a, ar, sum(ar)))

suma_divisores(0)
  
suma_divisores(11)

suma_divisores(17)

suma_divisores(23)

suma_divisores(12)

suma_divisores(18)

suma_divisores(24)