# por favor escribe aquí tu función
def es_primo(numero):
    if numero<=1:
        return False
    elif numero==2:
        return True
    else:
        for i in range(2,numero):
            i=i
            if numero%i==0:
                return False
        return True
for j in range(2, 200):
    print(j, "", es_primo(j))      


           