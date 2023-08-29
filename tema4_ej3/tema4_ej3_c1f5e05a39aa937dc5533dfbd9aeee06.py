palabra=input("Ingresa la palabra a traducir: ")
traduccion=""

for letra in palabra:
  if letra in "AEIOUaeiou":
    traduccion+=letra
    traduccion += "p" #Agregar p en cada sílaba de la palabra.
  traduccion += letra #Repetición de vocal.

print(traduccion)