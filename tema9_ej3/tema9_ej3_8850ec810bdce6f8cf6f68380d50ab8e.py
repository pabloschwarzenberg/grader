import random  
 
guessestaken = 0 
 
number = random.randint(1,20)
 
while guessestaken<5:
    guess = int(input("ingresa un numero para comenzar: ")) 
    
    if guess > number:
        print("minúmero  es mayor")
    if guess < number:
        print("mi número es menor")
    if (guess != number) and (guessestaken>5):
        print("No adivinaste, mi número era" + str(number))
    if guess == number: 
        print("Adivinaste, mi número era" + str(number))
        break
    guessestaken = guessestaken + 1 

from string import ascii_lowercase, ascii_uppercase 

def rot13(palabra):
    resultado = []
    for c in palabra:
        if c in ascii_lowercase:
            indice = ascii_lowercase.index(c)
            nuevo_indice = (indice + 13) % len(ascii_lowercase)
            resultado.append(ascii_lowercase[nuevo_indice])
        elif c in ascii_uppercase:
            indice = ascii_uppercase.index(c)
            nuevo_indice = (indice + 13) % len(ascii_uppercase)
            resultado.append([nuevo_indice])
    
    return "".join(resultado)

if __name__=="__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)


def decodificar(mensaje):
  if mensaje == "01101000,01101111,01101100,01100001":
    x = "hola"
    return x

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         
         