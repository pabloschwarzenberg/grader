def jerigonzo(texto):
    aux= ""
    es_vocal= ('a','e','i','o','u')
    
    for letra in texto:
        if not es_vocal(letra):
            aux+=letra
        else:
            aux+= letra+ "p"+ letra

    return aux
    