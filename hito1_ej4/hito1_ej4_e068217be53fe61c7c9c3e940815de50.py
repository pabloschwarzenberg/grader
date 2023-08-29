n=int(input("Convertir numero :"))
intento = []
resto1=n%2
intento.append(resto1)
while (n>1):
    Division = n//2
    n=Division
    Resto=Division%2
    intento.append(Resto)
intento.reverse()

print("resultado=",*intento,sep="")