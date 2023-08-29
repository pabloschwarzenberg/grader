def jerigonzo(string):
    palabra=list(string)
    for c in range(0,len(palabra)):
        letra=palabra[c]
        if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
            palabra[c]=(letra+'p'+letra)
    return ''.join(palabra)

if __name__ == "__main__":
    pass
         