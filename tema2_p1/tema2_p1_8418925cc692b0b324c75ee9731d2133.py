# por favor escribe aquí tu función
def es_primo (num):
    if num==1:
      return False
    primo = True
    for i in range(2,num):
        if num %i ==0:
            primo = False
    return primo
  