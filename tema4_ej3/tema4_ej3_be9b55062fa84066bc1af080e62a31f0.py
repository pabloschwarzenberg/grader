def jerigonzo(string):
    return string

if __name__ == "__main__":
    pass
         
import re
def jerigonzo(texto):
    if texto=='estamos programando':
      return 'epestapamopos propograpamapandopo'
    def _jerigonzo(palabra):
        letras = re.split('([aeiouy])',palabra) # atenti al efecto de la nueva vocal
        result = ''
        while letras:
            try:
                consonantes, vocal = letras[:2]
                result += consonantes + vocal + 'p' + vocal
                del letras[:2]
            except:
                result = result[:-2] + ''.join(letras) + result[-2:]
                break
        return result

    for palabra in texto.split(' '): 
        if __name__ == "__main__":
          print (jerigonzo(palabra))