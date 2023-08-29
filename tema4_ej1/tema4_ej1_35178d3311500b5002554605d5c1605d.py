import random
def ocultar_letras(palabra,cantidad):
    lista = []
    for x in palabra:
      lista.append(x)  
    i = 1
    while i <= cantidad:
      if lista[random.randint(0,len(lista)-1)] != "_":
        lista[random.randint(0,len(lista)-1)] = "_"
      else:
        i -= 1
      i += 1
    oculto = "".join(lista)
    return oculto 

def revisar_letra(palabra_secreta,palabra,letra):
    lista_palabra_secreta = []
    for x in palabra_secreta:
      lista_palabra_secreta.append(x)   
    lista_palabra = []
    for x in palabra:
      lista_palabra.append(x)
    i = 0
    if letra in lista_palabra_secreta:
      while i < len(lista_palabra):
        if lista_palabra[i] == "_" and lista_palabra_secreta[i] == letra:
          lista_palabra[i] = letra
        i += 1
    else:
      print("La letra no esta en la palabra")
    palabra_oculta = "".join(lista_palabra)
    return palabra_oculta
    

#lista = ["queso","morir","vivir","sushi","lepidoptero"]
#palabra = lista[random.randint(0,len(lista)-1)]
#print(ocultar_letras(palabra,3))
#oculto =ocultar_letras(palabra,3)
#print(revisar_letras(palabra,oculto,"o")

         