def rot13(palabra):
    codigo = ''
    for i in palabra:
        nerf = ord(i)
        if (nerf >= 65 and nerf <= 90) or (nerf >= 97 and nerf <= 122):
            if ((nerf + 13 > 90 and nerf + 13 <= 103) or (nerf + 13 > 122 and nerf + 13 <= 135)):
                codigo += chr(nerf - 13)
            else:
                codigo += chr(nerf + 13)
    return codigo

def whitda(palabra):
    Version1 = "abcdefghijklm"
    Version2 = "zyxwvutsrqpon"
    nerf = ""
    for i in range(len(palabra)):
        for a in range(len(Version1)):
            if Version1[a] == palabra[i]:
                nerf += Version2[a]
            elif Version2[a] == palabra[i]:
                nerf += Version1[a]
    return nerf
whitda("criptografia")
rot13("Criptografia")