def numero_perfecto(a):
  divisores_de_a=[i for i in range(1,a) if a %i==0]
  sda=0
  for _ in divisores_de_a:
    sda= sda + _
  
  if sda == a:
    return True 
  else:
    return False

if __name__=="__main__":
  a=int(input("Ingrese a: "))
  print(numero_perfecto(a))
           