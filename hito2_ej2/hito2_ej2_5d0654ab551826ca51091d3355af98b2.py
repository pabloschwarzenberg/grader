def adn_valido(secuencia):
    invalido=["b","d","e","f","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z"]
    secuencia.lower()
    i=0
    a=0
    while i<len(secuencia):
        if secuencia[i] in invalido:
            a+=1
            return "secuencia incorrecta"
        i+=1
    if a==0:
        return "secuencia correcta"

print(adn_valido(input()))
