def es_primo(n):
    for i in range(2,n):
        if (n%i==0):
            return False
        else:
          return True       
n=(input("Ingrese numero: "))
print(es_primo(n))