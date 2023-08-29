def numero_perfecto(a):
  suma_de_divisores=0
  for divisor in range(1,a):
    if a%divisor==0:
      suma_de_divisores=suma_de_divisores+divisor
  if suma_de_divisores==a:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           