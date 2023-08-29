def jerigonzo(string):
    sonante="aeiouAEIOUáéíóúÁÉÍÓÚ"
    frase=""
    letra="p"
    for x in range(len(string)):
        frase+=string[x]
        if string[x] in sonante and (not(string[x-1] in sonante) or x==0):
            frase+=letra
            frase+=string[x]
    string=frase
    return string

if __name__ == "__main__":
    string=input("que quiere decir: ")
    cambio=jerigonzo(string)
    print(cambio)

         