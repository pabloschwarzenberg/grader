if __name__ == "__main__": 
    word1 = input('Palabra 1? ')
    word2 = input('Palabra 2? ')
    def programa(word1,word2):
        if word1 == word2:
            return 'La distancia es 0, son iguales'
        if abs(len(word1)-len(word2)) >= 2:
            return 'Más de una operacion'
        if len(word1) == len(word2):
            g = 0
            contador = 0
            while g < len(word1):
                if word1[g] != word2[g]:
                    contador += 1
                g += 1
            if contador == 1:
                return '1 operacion (sustituir)'
            else:
                return 'Más de una operacion'
        if len(word1) > len(word2):
            h = 0
            neword = word1
            contador = 0
            while h < len(word2):
                while neword[h] != word2[h]:
                    contador += 1
                    neword = neword[:h]+neword[h+1:]
                    if len(neword) < len(word2):
                        h = len(word2)
                        break
                h += 1
            if contador == 1:
                return '1 operacion (insertar/borrar)'
            else:
                return 'Más de una operacion'
        if len(word1) < len(word2):
            h = 0
            neword = word2
            contador = 0
            while h < len(word1):
                while neword[h] != word1[h]:
                    contador += 1
                    neword = neword[:h]+neword[h+1:]
                    if len(neword) < len(word1):
                        h = len(word1)
                        break
                h += 1
            if contador == 1:
                return '1 operacion (insertar/borrar)'
            else:
                return 'Mas de una operacion'
    print(programa(word1,word2))

