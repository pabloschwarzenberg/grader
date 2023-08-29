# completa el código de la función
def suma_divisores(a):
  return
def suma_divisores(h):
    i = h - 1
    suma = 0
    while i > 0 :
       if h%i == 0 :
            suma = suma + i
            i = i - 1
       else:
            i = i - 1
   
    if suma == 1 :
        return suma, True
    else:
        return suma, False            