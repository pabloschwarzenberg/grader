def numero_perfecto(a):
  b = 1
  c = 0
  while b<a:
    if a%b==0:
      c = c+b
    b = b+1
  if a==c:
    return True
  else:
    return False

if __name__=="__main__":
  n = int(input("Ingrese un numero: "))
  e = 1
  g = 0
  while e<n:
    if numero_perfecto(f)==True:
      g = g+f
    e = e+1
  print("La suma de los numeros perfectos menores a ",n," es ",g)
           