import random
def ocultar_letras(palabra,cantidad):
    palabra = list(palabra)
    i = 1
    while i <= cantidad:
        j = random.randint(0,len(palabra)-1)
        if palabra[j] != "_":
            palabra[j] = "_"
            i = i+1
        else:
            continue
    palabra = "".join(palabra)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    l_s = list(palabra_secreta)
    l_p = list(palabra)
    i=0
    for elemento in palabra_secreta:
        if letra == elemento:
            if elemento == l_p[i]:
                i=i+1
            else:
                l_p[i] = letra
                i=i+1
        else:
            i = i+1       
    palabra = "".join(l_p)
    return palabra

if __name__ == "__main__":
    L = ["caleidoscopio","electroencefalograma","electrodomestico",
    "peritoneo","arteriosclerosis", "pterodactilo","radioinmunoanalisis",
    "socialdemocracia","desmitificar","contraindicacion"]
    n = random.randint(0,len(L)-1)
    p_secreta = L[n]
    cantidad = random.randint(1,len(p_secreta)-1)
    p_parcial = ocultar_letras(p_secreta,cantidad)
    print(p_parcial)
    i = 1
    while i <= 7:
        print("Este es el intento numero ",i,". Te quedan ",7-i," oportunidades")
        letra = input("Ingrese una letra o la palabra entera: ")
        if letra == p_secreta:
            print("Adivinaste!")
            break
        else:
            if len(letra) == len(p_secreta):
                print("Perdiste!")
                break
            else:
                actualizar = revisar_letra(p_secreta,p_parcial,letra)
                print(actualizar)
                p_parcial = actualizar
                if p_parcial == p_secreta and i != 7:
                    print("Adivinaste!")
                    break
                elif i == 7 and p_parcial != p_secreta:
                    print("Te quemaste!\nLa palabra era: ",p_secreta)                
        i=i+1
         