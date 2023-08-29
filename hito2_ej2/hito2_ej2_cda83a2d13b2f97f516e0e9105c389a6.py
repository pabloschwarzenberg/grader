s = input()
def secuencia_correcta(s) :
    lista_adn = list(s)
    letras_basura = list("bdefhijklmnopqrsuvwxyz")
    contador = 0
    for letra in lista_adn :
        if letra in letras_basura :
            print(letra)
            contador += 1
    if contador == 0:
        return "secuencia correcta"
    else :
        return "secuencia incorrecta"
print(secuencia_correcta(s))