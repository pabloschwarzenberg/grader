def rot13(palabra):
   abc = 'abcdefghijklmnopqrstuvwxyz'
   resultado = ''
   for letra in palabra:
       resultado += abc[(abc.find(letra)+13)%26]
   return resultado
           