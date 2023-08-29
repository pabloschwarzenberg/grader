# cifrado

abc = " abcdefghijklmnopqrstuvwxyz"

def rot13(frase):
    return "".join([abc[(abc.find(c) + 13) % 26] for c in frase])

if __name__ == "__main__":
    frase = input("Ingrese una frase: ")
    print(rot13(frase.lower()))
    
    