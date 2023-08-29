def jerigonzo(texto):
    string=""
    for letra in texto:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            string=string+letra+"p"+letra
        else:
            string=string+letra        
    return string
         