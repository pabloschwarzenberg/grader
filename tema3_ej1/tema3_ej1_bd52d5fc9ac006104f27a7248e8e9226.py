# completa el código de la función
def suma_divisores(a):
    cantidad = 0
    for x in range(1, a):
       if a % x == 0:
            cantidad += x
    if cantidad == 1:
        return cantidad,True
    else:
        return cantidad,False
  
             
      

