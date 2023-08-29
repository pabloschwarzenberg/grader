def es_primo(n):
    if n==1:
        return False
    elif n==2:
        return True
    elif n!=2 and n%2==0:
        return False
    
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True
if __name__ == "__main__":
  numero=int(input("Ingrese un numero: "))
  a = es_primo(numero)
  print(a)