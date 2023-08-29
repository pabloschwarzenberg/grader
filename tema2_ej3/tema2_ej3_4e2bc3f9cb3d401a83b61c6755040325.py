def numero_perfecto(c):
    Operacion = 0
    for j in range(1,c):
       if (c % (j) == 0):
          Operacion += (j)
    if c == Operacion:
       return True
    else:
       return False
           