def suma_divisores(a):
  b=a
  suma=0
  p=False
  while b>1:
    b-=1
    if a%b==0:
      suma+=b
  if suma==1:
    p=True
    
  return suma
def numero_perfecto(a):
  if suma_divisores(a)==a:
    return True
  return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           