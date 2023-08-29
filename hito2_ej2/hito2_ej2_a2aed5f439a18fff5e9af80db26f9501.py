from string import ascii_letters
s_l = list(ascii_letters)
print(s_l[0], s_l[2], s_l[6], s_l[19], s_l[26], s_l[28], s_l[32], s_l[45])
word = str(input())
word_l = list(word)
secuencia_adn = True
secuencia = False
for i in range (0,len(word)):
    if word_l[i] == s_l[0] or word_l[i] == s_l[2] or word_l[i] == s_l[6] or word_l[i] == s_l[19]or word_l[i] == s_l[26] or word_l[i] == s_l[28] or word_l[i] == s_l[32] or word_l[i] == s_l[45]:
        secuencia = True
    else:
        secuencia = False
    secuencia_adn = secuencia_adn and secuencia
if secuencia_adn:
    print ("secuencia correcta")
else:
    print("secuencia incorrecta")  