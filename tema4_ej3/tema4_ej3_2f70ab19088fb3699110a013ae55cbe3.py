def jerigonzo(texto):
    string=""
    for l in texto:
        if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
            string=string+l+"p"+l
        else:
            string=string+l        
    return string