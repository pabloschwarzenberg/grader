def numero_perfecto(a):
  suma=0
  for numero in range(1,a+1):
        if a % numero == 0 :
            suma =suma+numero
            print(suma)

  if (suma-a)!=a:
      return False
  if (suma-a)==a:
      return True

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))

