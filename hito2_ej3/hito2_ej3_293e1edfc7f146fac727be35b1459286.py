def subsecADN(adn,n):
    substrings = []
    subs_filtrados = []
    for i in range(0,len(adn)-n+1):
        substrings.append(adn[i:i+3])
    for substring in substrings:
        if substrings.count(substring) == 1:
            subs_filtrados.append(substring)
    if not subs_filtrados:
        print("ninguna")
    for adn in subs_filtrados:
        print(adn)

adn_ingresado = input()
n_ingresado = int(input())
subsecADN(adn_ingresado,n_ingresado)