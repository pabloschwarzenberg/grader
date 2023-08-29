def words_verification(a,b):
    if a == b:
        return "0D"
    else:
        return False

def words_len(a,b):
    largo_a = len(a)
    largo_b = len(b)
    if largo_a < largo_b:
        a = b
        b = a
        return len(a)
    elif largo_a > largo_b or largo_b == largo_a:
        return len(a)


def words_comparison(a,b):
    if len(a) == len(b):
        diferentes = []
        i = 0
        while i < words_len(a,b):
            if a[i] == b[i]:
                i += 1
            else:
                diferentes.append(a[i]+ b[i] + str(i))
                i +=1
        return diferentes
    elif len(a) != len(b):
        list_a = list(a)
        list_b = list(b)
        common_elements = set(list_a) & set(list_b)
        return common_elements

def letter_per(a):
    letter_str = str(a)
    letter = letter_str[2]
    return letter

def position_per(a):
    pos_str = str(a)
    pos = pos_str[4]
    return int(pos)

def replace_at(a, pos, letter):
    lista = list(a)
    lista[pos] = letter
    return "".join(lista)


def words_changing(a,b):
    if len(words_comparison(a,b)) > 2:
        return "+1"
    elif len(words_comparison(a,b)) == 1:
        if replace_at(a,position_per(a),letter_per(b)) == a:
            return "1S"
        else:
            return "IB"


def levenshtein(a,b):
    if words_verification(a,b) == False:
        return words_changing(a,b)
    else:
        return words_verification(a,b)

if __name__ == '__main__':
  a = input("Ingrese la primera palabra: ")
  b = input("Ingrese la segunda pregunta: ")
  print(levenshtein(a,b))