def alineamiento_adn(adn1,adn2):
    a=0
    b=0
    cadena=""
    while True:
        x=adn1[a]
        y=adn2[b]
        if x==y:
            cadena=cadena+(adn2[b])
            a=a+1
            b=b+1
        elif x!=y:
            cadena=cadena+("_")
            a+=1
        if a==len(adn1)-1:
            cadena=cadena+(adn2[b:len(adn2)])
            break
    return cadena
adn1=input()
adn2=input()
print(alineamiento_adn(adn1,adn2))