import random 
def ocultar_letras(palabra,cantidad):
    for i in range (cantidad):
        n2 = random.randint(0,len(palabra)-1)
        palabra = list(palabra)
        palabra[n2] = "_"
        palabra = "".join(palabra)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    if palabra_secreta.count(letra) != 0 and palabra_secreta.count(letra) != palabra.count(letra):
        for i in range (len(palabra)):
            if palabra_secreta[i] == letra:
                palabra = list(palabra)
                palabra[i] = letra
                palabra = "".join(palabra)
    return palabra

if __name__ == "__main__":
    lista = ["lepidoptero", "edificio", "casa", "tu hermana"]
    n = random.randint(0,len(lista)-1)
    menu = 1
    palabra_secreta = lista[n]
    n2 = random.randint(1,len(palabra_secreta)-1)
    a =(ocultar_letras(palabra_secreta, n2))
    print(a)
    while menu == 1:
        letra = input("letra")
        b =(revisar_letra(palabra_secreta, a, letra))
        print(b)
        a = b    
        if palabra_secreta == a:
            menu = 0
        
        
         