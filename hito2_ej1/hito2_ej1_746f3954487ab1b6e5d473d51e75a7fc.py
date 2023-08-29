def DNA_seq(s1, s2):
    resultado = ""
    i = 0
    for char in s1:
        if char == s2[i]:
            resultado = resultado + char
            i = i + 1
        else:
            resultado = resultado + "_"

    resultado = resultado + s2[i:]
    return resultado


str1 = input("Coloca el primer string: ")
str2 = input("Coloca el segundo string: ")

print("\n" + DNA_seq(str1, str2))