def ocultar_letras(palabra,cantidad):
    lista=list(palabra)
    import random
    i=random.randint(0,len(palabra))
    for j in range(0,cantidad):
        lista.pop(i)
        palabra=lista.insert(i,"_")
    palabra_secreta="".join(palabra)
    return palabra_secreta

def revisar_letra(palabra_secreta,palabra,letra):
    i=palabra_secreta.find("_")
    if letra==palabra[i]:
        return True
    else:
        return False
    
    return
    
if __name__ == "__main__":
    palabra=str(input("palabra:"))
    cantidad=int(input("cantidad:"))
    print(ocultar_letras(palabra,cantidad))
    palabra_secreta=ocultar_letras(palabra,cantidad)
    intentos=0
    while intentos<7:
        letra=str(input("adivine letra:"))
        revisar_letra(palabra_secreta,palabra,letra)
        if revisar_letra(palabra_secreta,palabra,letra)==True:
            print("correcto")
            break
        elif revisar_letra(palabra_secreta,palabra,letra)==False:
            print("incorrecto, intente nuevamente")
        intentos=intentos+1