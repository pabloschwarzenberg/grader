def rot13(palabra):
   abecedario = 'abcdefghijklmnopqrstuvwxyz'
   resultado = ''
   for letra in palabra:
       resultado += abecedario[(abecedario.find(letra)+13)%26]
   return resultado


 