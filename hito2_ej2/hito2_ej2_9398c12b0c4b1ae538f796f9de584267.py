def validar_adn(q):
    q=q.upper()
    for i in q:
        if (i is not "A") and (i is not "C") and(i is not "T") and(i is not "G"):
            return "secuencia incorrecta"
    return "secuencia correcta"
        
q=input()
print(validar_adn(q))
    