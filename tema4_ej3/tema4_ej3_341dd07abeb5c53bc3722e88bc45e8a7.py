def jerigonzo(stri):
    vocal = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    i = 0
    contador = 0
    stri = list(stri)
    while i < len(stri):
        for n in vocal:
            if stri[i] == n:
                stri[i] = stri[i] + "p" + stri[i]
        i += 1
    stri= "".join(stri)
    return stri
        
if __name__ == "__main__":
    pass
         