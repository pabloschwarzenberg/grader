def rot13(palabra):
    alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    cifrado = ''
    desplazamiento = 13
    for i in palabra.lower():
        if i in alfabeto:
            if alfabeto.index(i) < 13:
                cifrado += alfabeto[alfabeto.index(i) + 13]
            else:
                cifrado += alfabeto[alfabeto.index(i) - 13]

    return(cifrado)
  
           