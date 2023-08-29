#factores primos
def primo(numero):
    suma=0
    for i in range(2,numero):
        if numero%i==0:
            suma=suma+1
    if suma==0:
        return "si"
    else:
        return"no"

valor_entrada=int(input("Num: "))
while valor_entrada!=1:
    n=2
    while n<valor_entrada+1:

        if valor_entrada%n==0:
            if primo(n)=="si":
                valor_entrada=round(valor_entrada/n)
                print(n)
                break
        n=n+1
      