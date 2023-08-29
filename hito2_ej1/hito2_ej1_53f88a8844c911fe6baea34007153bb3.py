def alinear(ADN1,ADN2):
    #len(ADN1)>len(ADN2)
    adn_limpio=""
    x=0
    for i in range(len(ADN2)):
        while x<len(ADN1):
            if ADN2[i]!=ADN1[x]:
                adn_limpio+="_"
                x+=1
            else:
                adn_limpio+=ADN1[x]
                x+=1
                break
        if x==len(ADN1):
            x+=1
            continue
        if x>len(ADN1):
            adn_limpio+=ADN2[i]
    return adn_limpio

ADN1=input()
ADN2=input()
print(alinear(ADN1,ADN2))