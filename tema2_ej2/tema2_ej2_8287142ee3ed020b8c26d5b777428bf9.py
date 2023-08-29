def sumadivisores(n):
  suma = 0
  for i in range(1, n//2 + 1):
    if n % i == 0:
      suma += i
  return suma

def numerosamigos(a, b):
  sum_a = sumadivisores(a)
  sum_b = sumadivisores(b)

  return sum_a == b and sum_b == a

if __name__ == "__main__":
  num1 = int(input("Ingrese el primer número: "))
  num2 = int(input("Ingrese el segundo número: "))

  if numerosamigos(num1, num2):
    print("Los números", num1, "y", num2, "son amigos.")
  else:
    print("Los números", num1, "y", num2, "no son amigos.")
