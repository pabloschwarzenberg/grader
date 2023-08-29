# completa el código de la función
def amigos(a,b):
     divisoresA = []
     divisoresB = []
     for i in range(1, a):
        if a%i == 0:
            divisoresA.append(i)
     for i in range(1, b):
        if b%i == 0:
            divisoresB.append(i)
     if sum(divisoresA) == b:
         return True
     if sum(divisoresB) == a:
         return False
     else:
         return False
if __name__ == "__main__":    
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print(amigos(a,b))