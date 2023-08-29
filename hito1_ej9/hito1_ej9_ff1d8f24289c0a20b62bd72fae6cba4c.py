#Sistema de Ecuaciones
def suma_divisores(a):
  divisores=[i for i in range(1,a+1) if a%i==0]
  if divisores==1:
    return True
  else:
    return False
 
resultado= suma_divisores(7)
print(resultado)