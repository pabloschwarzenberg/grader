def numero_perfecto(a):
    numero = 0
    for i in range(1, a):
          if a%i == 0:
              numero +=i
    return numero == a
