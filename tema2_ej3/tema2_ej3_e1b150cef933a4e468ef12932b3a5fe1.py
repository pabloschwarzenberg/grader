def numero_perfecto(p):
    sumar = 0
    for a in range(1,p):
       if (p % (a) == 0):
          sumar = sumar + a
    if p == sumar:
       return True
    else:
       return False
           