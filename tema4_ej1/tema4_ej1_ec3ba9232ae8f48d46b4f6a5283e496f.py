import random
palabra=random.choice(["hola","perro","paralelepipedo","casa","tolerante","computador","teclado"])
if len(palabra)==4:
     cantidad=2
elif len(palabra)==5:
       cantidad=3
elif len(palabra)==14:
       cantidad=6
elif len(palabra)==9:
       cantidad=4
elif len(palabra)==10:
       cantidad=5
elif len(palabra)==7:
     cantidad=4
def ocultar_letras(palabra,cantidad):
     x=len(palabra)
     z=0
     k=list(palabra)
     while z!=cantidad:
      k=list(k)
      h=random.randint(0,x-1)
      if k[h]!="_":
       k[h]="_"
       k=str("".join(k))
       z=z+1
      else:
        k=k
     return k

def revisar_letra(palabrasecreta,palabra_dicha,letra):
        if (letra in palabra):
            palabrasecreta=list(palabrasecreta)
            palabrasecreta[palabra.find(letra)]=letra
            palabrasecreta=str("".join(palabrasecreta))
            return palabrasecreta
        else:
            return "no existe la letra en la palabra secreta"
        if palabra_dicha==palabra:
            return "haz conseguido adivinar la palabra"
        elif palabra_dicha!=palabra:
            return"Lo siento, no es la palabra"
if __name__ == "__main__":

  print(revisar_letra(ocultar_letras(palabra,cantidad),0,letra))
 