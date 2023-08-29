def jerigonzo(tex):
    jerigonzo_texto = ""
    voc = "aeiouAEIOU"
    
    for letra in tex:
        jerigonzo_texto += letra
        if letra in voc:
            jerigonzo_texto += "p" + letra.lower()
    
    return jerigonzo_texto

if __name__ == "__main__":
    tex = input("Ingrese un tex: ")
    texto_traducido = jerigonzo(tex)
    print("Texto traducido a jerigonzo:", texto_traducido)

         