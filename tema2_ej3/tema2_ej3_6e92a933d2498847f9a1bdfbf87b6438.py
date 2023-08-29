def suma_divisores(a):
  divs=[]
  prueba=1
  while prueba<a:
    if a%prueba==0:
      divs.append(prueba)
    prueba+=1
  return sum(divs)
    
def numero_perfecto(a):
    if suma_divisores(a)==a:
      return True
    else:
      return False

