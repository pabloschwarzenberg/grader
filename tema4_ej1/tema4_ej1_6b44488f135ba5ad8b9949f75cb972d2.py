def ocultar_letras(palabra,cantidad):
    a=list(palabra)
    for i in range(cantidad):
      import random
      x=random.randint(0,len(palabra)-1)
      while a[x]=="_":
        x=random.randint(0,len(palabra)-1)
      a[x]="_"
      word="".join(a)
    return word

def revisar_letra(palabra_secreta,palabra,letra):
    a=list(palabra_secreta)
    b=list(palabra)
    for i in range(len(a)):
        if letra==a[i]:
            b[i]=letra
    palabra="".join(b)
    return palabra

if __name__ == "__main__":
    lista=["esquimal", "elefante", "computador", "integral", "ornitorrinco"]
    intentos=7
    import random
    palabra_secreta=lista[random.randint(0,4)]
    palabra=ocultar_letras(palabra_secreta,random.randint(0,len(palabra_secreta)-1))
    print(palabra)
    while intentos>0:
      letra=input("Ingresa letra: ")
      palabra=revisar_letra(palabra_secreta,palabra,letra)
      if palabra==palabra_secreta:
          print(palabra)
          print("Felicidades, adivinaste la palabra")
          break
      else:
          print(palabra)
      intentos=intentos-1
    if palabra!=palabra_secreta:
        print("No tienes mas intentos. La palabra era: "+palabra_secreta)