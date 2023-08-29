def rot13(palabra):
    lista=list(palabra)
    abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    cambio_letra=["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
    nueva=""
    for i in lista:
        nueva+=cambio_letra[abecedario.index(i)]
    return nueva

           