
import random

def ocultar_letras(palabra_secreta, cantidad):
    palabra_1 = list(palabra_secreta)
    pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    i = 1
    while i <= cantidad:
        posicion = int(random.choice(pos))
        palabra_1[posicion] = "_"
        palabra_2 = "".join(palabra_1)
        pos.remove(posicion)
        i += 1
    return (palabra_2)

def revisar_letra(palabra_secreta, palabra, x):
   
    if x == palabra_secreta:
        return (palabra_secreta)
    
    palabra = list(palabra)
    palabra_secreta = list(palabra_secreta)
    
    i = 0
    while i < len(palabra):
         
        if palabra[i]=="_":
            if palabra_secreta[i] == x:
                palabra[i] = x
        
        i += 1
    return ("".join(palabra))

if __name__ == "__main__":
    revisar = revisar_letra("lepidoptero", "le_i_opter_" , "o")
    print(revisar)
