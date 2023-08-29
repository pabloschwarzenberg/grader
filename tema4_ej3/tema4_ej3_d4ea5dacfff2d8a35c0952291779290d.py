def jerigonzo(texto):
    aux=""
    for letra in texto:
        if not es_vocal(letra):
            aux+=letra
        else:
            aux+=letra+"p"+letra
    return aux
    

if __name__ == "__main__":
    palabra=str(input("Ingrese la palabra que quiere transformar al jerigonzo:"))
    jerigonzo(palabra)
    
         