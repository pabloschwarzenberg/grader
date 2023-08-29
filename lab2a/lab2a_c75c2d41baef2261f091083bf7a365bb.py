numero1=int(input('Inserte numero de inicio: ' ))
numero2=int(input('Inserte numero final: ' ))

while numero1<=numero2:
    c=numero1%2
    c1=numero1%7
    if c==0 and c1==0:
        print(numero1)
    numero1=numero1 +1