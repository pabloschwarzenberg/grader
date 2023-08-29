def jerigonzo(palabra):
    cambio=""
    
    for letra in palabra:
      if letra in "AEIOUaeiou":
        cambio=cambio+letra
        cambio=cambio+"p"
      cambio=cambio+letra
    
    return cambio
a=jerigonzo("hola")
print(a)