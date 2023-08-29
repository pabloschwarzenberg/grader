import random
palabras=["lepidoptero","zagal","jan","jodelaperra"]
palabra=random.choice(palabras)
b=len(palabra)
n=list(palabra)
cantidad = random.randint(1,b)
intentos=7
def ocultar_letras(palabra, cantidad):
    for x in range(cantidad):
        c = n[random.randint(0, b)]
        palabra2 = palabra.replace(c, '_')
    return(palabra2)

def revisar_letra(palabra,palabra2,letra):
    global intentos
    while intentos>0:
        for i in range(1,b):
            j = palabra.find(letra)
            if j==-1:
                print("Esa letra ya está")
                intentos-=1
                letra = str(input("Ingrese una letra:"))
            if j!=-1 and j!="_":
                print("Esa letra ya está")
                intentos-=1
                letra = str(input("Ingrese una letra:"))
            elif j!=-1 and j=="_":
                palabra2.replace("_","letra")
                print(palabra2)
                intentos-=1
                letra = str(input("Ingrese una letra:"))
    return palabra2
         