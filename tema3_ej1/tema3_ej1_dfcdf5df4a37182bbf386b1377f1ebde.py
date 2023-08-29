
def es_primo(x):
    if x==1:
        return False
    if x == 2:
        return True
    else:
        for number in range(3, x):
            if x%number==0 or x%2==0:
                return False
        return True

def suma_divisores(a):
  i=1
  suma=0
  while i<a:
    if a%i==0:
       suma=suma+i
    i=i+1
  return (suma,es_primo(a))




if __name__ == "__main__":
  a=int(input())  
  suma_divisores(a)
  es_primo(a)
  