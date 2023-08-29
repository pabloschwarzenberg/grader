# por favor escribe aquí tu función
def es_primo(numero):
    a=numero%2
    if numero==2 and a==0:
        return ("true")
    elif numero==1:
        return ("false")
    elif a!=0:
        return("true")
    else:
        return ("false")

if __name__ == "__main__":
  N=int(input())