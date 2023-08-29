def jerigonzo(string):
    a=""
    for letra in string:
        if letra in "aeiouAEIOU":
            a+=letra
            a+="p"
        a+=letra
    return a
         