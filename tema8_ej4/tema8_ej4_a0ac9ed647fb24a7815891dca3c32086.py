def rot13(palabra):

    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    string = ""
    
    for k in palabra:
        if k in alfabeto:
            if alfabeto.index(k) < 13:
                string += alfabeto[alfabeto.index(k) + 13]
                
            else:
                string += alfabeto[alfabeto.index(k) - 13]

        elif k in alfabeto.upper():
             if alfabeto.upper().index(k) < 13:
                 string += alfabeto.upper()[alfabeto.upper().index(k) + 13]
                 
             else:
                string += alfabeto.upper()[alfabeto.upper().index(k) - 13]
        else:
            string += 1

    return string