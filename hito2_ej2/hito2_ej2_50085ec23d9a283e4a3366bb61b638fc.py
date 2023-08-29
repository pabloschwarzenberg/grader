adn=input("Ingrese Secuencia: ")
adn=adn.upper()
i=0
ver=0
fal=1
while i<len(adn):
    if (adn[i]=="A"):
        ver=ver+1
    elif (adn[i]=="C"):
        ver=ver+1
    elif (adn[i]=="T"):
        ver=ver+1
    elif (adn[i]=="G"):
        ver=ver+1
    else:
        fal=fal+1
    i+=1

if fal>1:
    print("Secuencia Incorrecta")
else:
    print("Secuencia Correcta")