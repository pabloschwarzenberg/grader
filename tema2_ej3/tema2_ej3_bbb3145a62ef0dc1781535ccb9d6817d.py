def numero_perfecto(m):
    suma = 0
    for p in range(1,m):
       if (m % (p) == 0):
          suma += (p)
    if m == suma:
       return True
    else:
       return False