def jerigonzo(string):
    list_p_vocal = ["pa", "pe", "pi", "po", "pu"]
    list_vocal = ["a", "e", "i", "o", "u"]
    list_pos_p = []
    list_pos_v = []
    string = list(string)
    
    for letra in range(len(string)):
        for vocal in range(len(list_vocal)):
            if string[letra] == list_vocal[vocal]:
                list_pos_p.append(string[letra])
                list_pos_v.append(vocal)

    frase = ""
    
    for a in range(len(string)):
        b = 0
        while b < len(list_pos_p):
            if list_pos_p[b] == string[a]:
                frase = frase + string[a] + list_p_vocal[list_pos_v[b]]
                b = True
                break
            b += 1
        if b != True:
            frase = frase + string[a]                
    return frase


if __name__ == "__main__":
    pass
         