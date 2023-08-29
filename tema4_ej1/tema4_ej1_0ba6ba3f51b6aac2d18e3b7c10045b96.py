import random
def ocultar_letras(palabra,cantidad):
    palabra=list(palabra)
    guion="_"
    guiones=[]
    while len(guiones)<cantidad:
        guiones.append(guion)
    while len(guiones)!=0:
        i=random.randint(0,cantidad)
        posicion=palabra[i]
        if posicion=="_":
            continue
        elif posicion!="_":
            espacio=guiones.pop(0)
            palabra[i]=espacio
    palabra="".join(palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    palabra_secreta=list(palabra_secreta)
    palabra=list(palabra)
    i=0
    while i<len(palabra):
        if letra in palabra:
            if palabra[i]==letra:
                palabra_secreta[i]=letra
                i=i+1
            elif palabra[i]!=letra:
                i=i+1
        elif letra not in palabra:
            return 'la letra no corresponde a la palabra'
        
    palabra_secreta=''.join(palabra_secreta)
    return palabra_secreta

if __name__ == "__main__":
    print('Vamos a jugar!!!! adivina mi palabra secreta...')
    palabras=["bandera","camisa","neumatico","cardumen","motor"]
    palabra=random.choice(palabras)
    cantidad=random.randint(1,len(palabra))
    palabraSecreta=ocultar_letras(palabra,cantidad)
    print('la palabra es:',palabraSecreta)
    opcion=input('¿desea escribir la palabra completa o a letra? (dijite palabra o letra):')
    if opcion=='letra':
      c=0
      while palabraSecreta!=palabra and c==cantidad:
        frase=input('ingresa letra:')
        semipalabra=revisar_letra(palabraSecreta,palabra,frase)
        print(semipalabra)
        c=c+1
        if semipalabra==palabra:
          print('adivinaste!, mi palabra era:',palabra)
        elif c==3:
          print('No adivinaste :c, mi palabra era:',palabra)
    elif opcion=='palabra':
      frase=input('ingrese palabra:')
      if frase==palabra:
          print('adivinaste!, mi palabra era:',palabra)
      else:
          print('No adivinaste :c, mi palabra era:',palabra)


    pass
         