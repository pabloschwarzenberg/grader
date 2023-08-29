def jerigonzo(string):
    vocales=["a","e","i","o", "u"]
    lista_palabra=list(string)
    palabra_nueva=[]
    for letra in lista_palabra:
        if letra not in vocales:
            palabra_nueva.append(letra)
        if letra in vocales:
            palabra_nueva.append(letra)
            palabra_nueva.append("p")
            palabra_nueva.append(letra)        
    string="".join(palabra_nueva)
    return (string)

if __name__ == "__main__":
    pass
         