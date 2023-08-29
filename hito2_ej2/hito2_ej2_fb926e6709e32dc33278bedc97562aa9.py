def adn(secuencia):
    secuencia=secuencia.upper()
    a=0
    for letra in secuencia:
        if letra!="A" and letra!="T" and letra!="C" and letra!="G":
            a+=1
    if a==0:
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")
        
a=input()
adn(a)