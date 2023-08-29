from random import randint
def ocultar_letras(palabra,cantidad):
    palabra1 = ""
    lista = []
    a = randint(0,len(palabra)-1)
    for i in range(cantidad):
      while a in lista:
        a = randint(0,len(palabra)-1)
      l = list(palabra)
      l[a] = "_"
      palabra = "".join(l)
      lista.append(a)
    return (palabra)  
def revisar_letra(palabra_secreta,palabra,letra):
    lista4 = []
    lista3 = []
    lista2 = []
    fallas = True
    
    cont = 0
    for h in palabra_secreta:
       if letra == palabra_secreta:
        palabra = palabra_secreta
        return palabra
       elif letra in h:
        l = list(palabra)
        l[cont] = letra
        palabra = "".join(l)
        lista4.append(cont)
        lista3.append(palabra)
        print(palabra)
        if lista3[-1]==palabra_secreta:
          return palabra    
          if fallas == 0:
            return palabra
        lista2.append(letra)
       cont+=1   

    return palabra







if __name__ == "__main__":
  lista = ["hola","como","estas"]
  numero = randint(0,2)
  palabra = lista[numero]
  palabra_secreta = lista[numero]
  cantidad = randint(1,len(palabra))
  c = ocultar_letras(palabra,cantidad)
  print(c)
  letra = input()
  print(revisar_letra(palabra_secreta,c,letra))
