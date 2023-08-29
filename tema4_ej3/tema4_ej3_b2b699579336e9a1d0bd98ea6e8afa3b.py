def jerigonzo(string):
    vocales=["a","e","i","o","u"]
    p_jer=""
    for i in range(len(string)):
        p_jer=p_jer+string[i]
        for j in vocales:
            if j== string[i]:
                p_jer=p_jer+"p"+j
    return(p_jer)

if __name__ == "__main__":
    pass
         