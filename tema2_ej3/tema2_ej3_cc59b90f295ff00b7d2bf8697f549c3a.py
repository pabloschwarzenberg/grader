def numero_perfecto(a):
  suma = 0

  for i in range(1,a):
    if a % i == 0:# and not i == a:
      suma += i
  return  suma == a

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))



