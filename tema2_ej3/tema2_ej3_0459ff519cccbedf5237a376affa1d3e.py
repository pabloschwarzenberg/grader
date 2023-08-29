#numeros perfectos
def numero_perfecto(y):
    s = 0
    for x in range(1,y):
       if (y % (x) == 0):
          s += (x)
    if y == s:
       return True
    else:
       return False