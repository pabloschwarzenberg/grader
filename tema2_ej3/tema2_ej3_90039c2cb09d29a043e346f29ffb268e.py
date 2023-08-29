def numero_perfecto(a):
  x=1
  suma=0
  while x<a:
    if a%x==0:
      suma=suma+x
      x=x+1
    else:
      x=x+1
  if a==suma:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           