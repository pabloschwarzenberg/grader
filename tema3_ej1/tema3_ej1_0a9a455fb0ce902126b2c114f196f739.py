def SumaDeDivisores(num):
  es_primo = False
  divisores = [1,num-1]
  suma = 0
  for numero in divisores:
    division = num/numero
    suma += division
    
  if num % numero == num and num % numero == 1:
    return True
    print("Es primo")
  return suma, False

if __name__ == "__main__":
  a = int(input("ingrese un numero: "))
  print(SumaDeDivisores(a))