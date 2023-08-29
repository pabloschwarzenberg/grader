def numero_perfecto(w):
    x = 0
    for p in range(1,w):
       if (w % (p) == 0):
          x += (p)
    if w == x:
       return True
    else:
       return False

           