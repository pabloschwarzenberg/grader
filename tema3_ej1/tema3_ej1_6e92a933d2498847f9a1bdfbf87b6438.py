# completa el código de la función
def suma_divisores(a):
  divs=[]
  prueba=1
  primo=False
  while prueba<a:
    if a%prueba==0:
      divs.append(prueba)
    prueba+=1
  if sum(divs)==1:
    return sum(divs),True
  else:      
    return sum(divs),False
           