def jerigonzo(string):
    palabra = ""
    vocal = ["a", "e", "i", "o", "u"]
    for i in string:
        if i in vocal:
            palabra += i
            palabra += "p"
            palabra += i
        else:
            palabra +=i
    return palabra
def rot13(palabra):
   abecedario = "abcdefghijklmnopqrstuvwxyz"
   resultado = ""
   for letra in palabra:
       resultado += abecedario[(abecedario.find(letra)+13)%26]
   return resultado
         