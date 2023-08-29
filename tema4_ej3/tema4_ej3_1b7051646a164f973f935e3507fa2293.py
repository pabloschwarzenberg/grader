def jerigonzo(palabra):
 jerigonza = ""
 for letra in palabra:
   jerigonza += letra
   if letra in "AEUOUaeiou":
        # agregar p despues de la vocal
        jerigonza += "p"
        # repetir la vocal
        jerigonza += letra
 return (jerigonza)

if __name__ == "__main__":
#  palabra = input("Ingresa una palabra: ")
#  salida=jerigonzo("estamos programando")
#  print (salida)
 pass