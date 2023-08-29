adn=input("String: ")
n=int(input("n: "))
contador=0
contador_general=0
for i in range(len(adn)):
    j=i+3
    if j <=len(adn):
        palabra1=adn[i:i+n]
        contador=0
        for y in range(len(adn)):
            x=y+3
            if x <=len(adn):
                palabra2=adn[y:y+n]
                if palabra1==palabra2:
                    contador+=1
        if contador==1:
            print(palabra1)
            contador_general+=1           
if contador_general==0:
    print("ninguna")     