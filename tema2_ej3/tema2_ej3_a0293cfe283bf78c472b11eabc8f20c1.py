def numero_perfecto(a):
    sumar = 0
    for i in range(1,a):
       if (a % (i) == 0):
          sumar += (i)
    if a == sumar:
       return True
    else:
       return False