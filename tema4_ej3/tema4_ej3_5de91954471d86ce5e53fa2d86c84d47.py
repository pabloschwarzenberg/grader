def jerigonzo(string):
    string2=''
    cadena=''
    for letra in string.lower():
        cadena+=letra
        if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
            string2+=cadena+'p'+letra
            cadena=''
    string=string2
    return string

if __name__ == "__main__":
    pass
         