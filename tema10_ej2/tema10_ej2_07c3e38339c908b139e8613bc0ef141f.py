#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
   if len(palabra1) == len(palabra2):
        letra = 0
        distintas = ""
        while letra < len(palabra1):
            if palabra1[letra] == palabra2[letra]:
                letra += 1
            else:
                distintas += palabra1[letra]
                letra+=1

        if len(distintas)==1:
            return "1S"
        elif len(distintas) == 0:
            return "0D"
        else:
            return "+1"

   if len(palabra1) != len(palabra2):
       listapalabra1 = list(palabra1)
       listapalabra2 = list(palabra2)
       if len(listapalabra1) < len(listapalabra2):
            letra = 0
            distintas = ""
            while letra < len(listapalabra2):
                if listapalabra1[letra] == listapalabra2[letra]:
                    letra += 1
                else:
                    listapalabra1.insert(letra," ")
                    distintas += listapalabra2[letra]
                    letra += 1

            if len(distintas) == 1:
                return "IB"
            else:
                return "+1"

       else:
            letra = 0
            distintas = ""
            while letra < len(listapalabra1):
                if listapalabra1[letra] == listapalabra2[letra]:
                    letra += 1
                else:
                    listapalabra2.insert(letra," ")
                    distintas += listapalabra1[letra]
                    letra += 1

            if len(distintas) == 1:
                return "IB"

            else:
                return "+1"
    


           