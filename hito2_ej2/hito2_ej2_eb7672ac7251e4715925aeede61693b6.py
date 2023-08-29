adn=str(input())
dna=list(adn)
letras=["a","c","t","g"]
for x in dna:
    if x!=letras:
        print("secuencia incorrecta")
    else:
        print("secuencia correcta")
