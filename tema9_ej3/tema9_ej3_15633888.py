def bin_to_dec(bin8):
    bin8=str(bin8)
    dec=0
    for w in range(8):
        if bin8[w]==0:
            pass
        else:
            dec+=int(bin8[w])*2**(7-w)
    return dec

def string_4num_bin_to_lista_dec(mensajex):
    lista_binarios=mensajex.split(",")
    lista_decimales=[]
    for j in lista_binarios:
        lista_decimales.append(bin_to_dec(j))
    return lista_decimales

def lista_dec_to_lista_caracteres(pepsi):
    lista_caracteres=[]
    for y in pepsi:
        lista_caracteres.append(chr(y))
    return lista_caracteres

def lista_caracteres_to_the_rial(monster):
    word="".join(monster)
    return word
def decodificar(mensaje):
    happy=lista_caracteres_to_the_rial(lista_dec_to_lista_caracteres(string_4num_bin_to_lista_dec(mensaje)))
    return happy

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         