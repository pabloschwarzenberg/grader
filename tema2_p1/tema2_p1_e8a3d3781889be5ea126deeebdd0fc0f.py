#Numeros  primos
def es_primo(num):
    es_primo = bool()
    x = 1
    if (num >= 2):
        for i in range(2, num):
            if (num % i == 0):
                es_primo = False
                return es_primo
                break
            else:
                es_primo = True
    return es_primo
if __name__ == "__main__":
  n=int(input("ingrese numero: "))
  result=primo(n)
  print(result)
