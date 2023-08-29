#Distancia Levenshtein
def levenshtein(word1,word2):
    if word1 == word2:
        return '0D'
    if abs(len(word1)-len(word2)) >= 2:
        return '+1'
    if len(word1) == len(word2):
        g = 0
        contador = 0
        while g < len(word1):
            if word1[g] != word2[g]:
                contador += 1
            g += 1
        if contador == 1:
            return '1S'
        else:
            return '+1'
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
            return 'IB)'
        else:
            return '+1'
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
            return 'IB'
        else:
            return '+1'