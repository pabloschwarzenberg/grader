def jerigonzo(frase):
    vocales=['a','e','i','o','u','A','E','I','O','U'] 
    for vocal in vocales: 
        frase=frase.replace(vocal,vocal+"p"+vocal.lower()) 
    return frase

if __name__ == "__main__":
    a=input("ingrese palabra: ")
    frase=jerigonzo(a)
    print(frase)
    pass
         