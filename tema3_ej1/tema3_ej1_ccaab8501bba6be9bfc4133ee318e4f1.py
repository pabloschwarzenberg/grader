def suma1(a):
    divisores=[1]
    if a==1:
        divisores=0
        return divisores
    for i in range(2,a-1):
        if a % i==0:
            divisores.append(i)
    return sum(divisores)

def primo(suma):
    if suma==0:
        return False
    for n in range(2, suma):
        if suma % n == 0:
            return False
    return True

def suma_divisores(a):
    return(suma1,primo)
if __name__ == "__main__":
  a=input("")
  suma_divisores(a)
