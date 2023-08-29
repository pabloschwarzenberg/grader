import random
palabras=['jose','juan','ramon','juanita']
largo = len(palabras)
indice = random.randint(0,largo-1)
palabra_ = palabras[indice]
adivinando = [] 
def ocultar_letra():
    lineas = ""
    if len(adivinando) == 0:
        for letra in palabra_:
           adivinando.append("_") 
    
    for letra in adivinando:
       
        lineas = lineas + letra + " "
    
    
def revisar_letra(letra,palabra):
    existe = 0
    for i in range(len(palabra)):
        if palabra[i] == letra:
            existe = 1
            reemplazarLetra(i,letra, adivinando)
    return existe