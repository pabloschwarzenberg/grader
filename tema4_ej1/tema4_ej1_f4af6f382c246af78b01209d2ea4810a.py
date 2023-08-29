import random

letras_borradas = ""
p_list = []

def ocultar_letras(palabra,cantidad):
    global letras_borradas
    global pos_borradas
    global p_list
    palabra_nueva = ""
    p_list = []
    pos_usadas=""
    i = 0
    while i < len(palabra):
        p_list.append(palabra[i])
        i += 1
    while cantidad != 0:
        pos = str(random.randint(0,len(palabra)-1))
        if pos not in pos_usadas:
            pos_usadas = pos_usadas + pos
            letras_borradas = letras_borradas + p_list[int(pos)] + pos
            p_list.pop(int(pos))
            p_list.insert(int(pos),"_")
            cantidad -= 1
    i = 0
    while i < len(p_list):
        palabra_nueva = palabra_nueva + p_list[i]
        i += 1
    return palabra_nueva

def revisar_letra(palabra_secreta,palabra,letra):
    global letras_borradas
    if len(letra) != 1:
        if letra == palabra_secreta:
            return palabra
        else:
            pass
    else:
        palabra_nueva = ""
        if letra in letras_borradas:
            i = 0
            while True:
                if letras_borradas[i] == letra:
                    p_list.pop(int(letras_borradas[i+1]))
                    p_list.insert(int(letras_borradas[i+1]),letras_borradas[i])
                    i = 0
                    while i < len(p_list):
                        palabra_nueva = palabra_nueva + p_list[i]
                        i += 1
                    return palabra_nueva
                i+=1                
        else:
            pass
"""

if __name__ == "__main__":
    l = ['holaa','algo','casa']
    a = input() #l[random.randint(0,len(l)-1)]
    letr = "a"
    cant = random.randint(1,len(a))
    
    print(ocultar_letras(a,cant))
    #print(letras_borradas)
    while True:
        ingresado = input()
        print(revisar_letra(a,letr,ingresado))
"""