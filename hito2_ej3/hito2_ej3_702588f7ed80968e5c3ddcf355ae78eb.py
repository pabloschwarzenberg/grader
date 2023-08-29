secuencia=input("ingrese secuencia de ADN",)
largosecuencia=len(secuencia)
largosc=int(input("ingrese largo",))
n=0

n=0
for secuenciacorta in secuencia:
    secuenciacorta=secuencia[n:(n+largosc)] 
    toddy=secuencia.count(secuenciacorta)
    if toddy==1:
        print(secuenciacorta)
    else:
        print("ninguna")
    n=n+largosc

n=1
for secuenciacorta in secuencia:
    secuenciacorta=secuencia[n:(n+largosc)] 
    toddy=secuencia.count(secuenciacorta)
    if toddy==1:
        print(secuenciacorta)
    else:
        print("ninguna")
    n=n+largosc

n=2
for secuenciacorta in secuencia:
    secuenciacorta=secuencia[n:(n+largosc)] 
    toddy=secuencia.count(secuenciacorta)
    if toddy==1:
        print(secuenciacorta)
    else:
        print("ninguna")
    n=n+largosc

