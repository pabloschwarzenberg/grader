def alineamiento_ADN(and1,adn2):

    o=0
    p=0
    ult=""

    while True:

        x=adn1[o]
        y=adn2[p]

        if x==y:
            ult=ult+(adn2[p])
            o=o+1
            p=p+1

        elif x!=y:
            ult=ult+("_")
            o=o+1            

        if o==len(and1)-1:
            ult=ult+(adn2[p:len(adn1)])
            break

    return(ult)

adn1=input()
adn2=input()

print(alineamiento_ADN(adn1,adn2))

