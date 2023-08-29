def rot13(palabra):
    lista=list(palabra)
    posicion=0
    for i in lista:
      if i.lower()=="a":
        lista[posicion]='n'
      elif i.lower()=="b":
        lista[posicion]='o'
      elif i.lower()=="c":
        lista[posicion]='p'
      elif i.lower()=="d":
        lista[posicion]='q'
      elif i.lower()=="e":
        lista[posicion]='r'
      elif i.lower()=="f":
        lista[posicion]='s'
      elif i.lower()=="g":
        lista[posicion]='t'
      elif i.lower()=="h":
        lista[posicion]='u'
      elif i.lower()=="i":
        lista[posicion]='v'
      elif i.lower()=="j":
        lista[posicion]='w'
      elif i.lower()=="k":
        lista[posicion]='x'
      elif i.lower()=="l":
        lista[posicion]='y'
      elif i.lower()=="m":
        lista[posicion]='z'
      elif i.lower()=="n":
        lista[posicion]='a'
      elif i.lower()=="o":
        lista[posicion]='b'
      elif i.lower()=="p":
        lista[posicion]='c'
      elif i.lower()=="q":
        lista[posicion]='d'
      elif i.lower()=="r":
        lista[posicion]='e'
      elif i.lower()=="s":
        lista[posicion]='f'
      elif i.lower()=="t":
        lista[posicion]='g'
      elif i.lower()=="u":
        lista[posicion]='h'
      elif i.lower()=="v":
        lista[posicion]='i'
      elif i.lower()=="w":
        lista[posicion]='j'
      elif i.lower()=="x":
        lista[posicion]='k'
      elif i.lower()=="y":
        lista[posicion]='l'
      elif i.lower()=="z":
        lista[posicion]='m'
      final=''.join(lista)
      posicion+=1

    return final
        

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           