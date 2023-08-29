def numero_perfecto(a):
  y = 0
  perfecto = False
  for x in range(1,a):
    if a%x == 0:
      y += x
  if y == a:
      perfecto = True
  return perfecto
    
    
    

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           