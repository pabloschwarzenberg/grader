def numero_perfecto(a):
  suma=0

  for i in range(a//2):
    if a%(i+1)==0:
      suma+=(i+1)
    
  if a==suma:
    return True
  else:
    return False
    


if __name__=="__main__":
  a=int(input("Ingrese a: "))
  print(numero_perfecto(a))