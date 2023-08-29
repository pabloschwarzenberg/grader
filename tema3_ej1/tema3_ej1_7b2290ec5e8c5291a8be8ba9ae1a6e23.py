def suma_divisores(a):

    b = int(a)
    
    suma = 0
    is_primo = False
    
    for i in range(1, b):
      if b%i == 0 and i<b:
        suma = suma + i
    
    if suma == 1:
      is_primo = True

    return suma, is_primo