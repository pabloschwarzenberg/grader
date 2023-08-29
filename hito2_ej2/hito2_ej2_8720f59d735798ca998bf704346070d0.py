x=input()
adn="atgcATGC"
suma=0
for a in x:
    if adn.find(a)==-1:
        suma+=1
if suma==0:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")