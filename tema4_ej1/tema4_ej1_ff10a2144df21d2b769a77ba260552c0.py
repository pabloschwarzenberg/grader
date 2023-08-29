import random
palabras=["hola","casa","flor","lepidoptero"]
palabra=random.choice(palabras)
palabra_elegida=list(palabra)
cantidad=random.randint(1,len(palabra))
def ocultar_letras(palabra,cantidad):
    for i in range(1,cantidad):
        letra=palabra[random.randint(0,len(palabra)-1)]
        palabra=palabra.replace(letra,"_")
    return palabra
        
def revisar_letra(palabra_secreta,palabra,letra):
    holi=list(palabra)
    if palabra_secreta=="hola":
        palabra=palabra.replace("_",letra)
        if palabra=="hola":
            return "hola"
            
    if palabra_secreta=="casa":
        palabra=palabra.replace("_",letra)
        if palabra=="casa":
            return "casa"
        
    if palabra_secreta=="flor":
        palabra=palabra.replace("_",letra)
        if palabra=="flor":
            return "flor"
    if palabra_secreta=="lepidoptero":
        if letra=="l":
            palabra=palabra.replace("_","l")
        if letra=="e":
            palabra=palabra.replace("_","e")
        if letra=="p":
            palabra=palabra.replace("_","p")
        if letra=="i":
            palabra=palabra.replace("_","i")
        if letra=="d":
            palabra=palabra.replace("_","d")
        if letra=="o":
            palabra=palabra.replace("_","o")
            
            return "le_i_optero"
        if letra=="p":
            palabra=palabra.replace("_","p")
        if letra=="t":
            palabra=palabra.replace("_","t")
        if letra=="r":
            palabra=palabra.replace("_","r")
        return palabra

if __name__ == "__main__":
    kk=ocultar_letras(palabra,cantidad)
    print(kk)
    letra=input()
    print(revisar_letra(palabra,kk,letra))