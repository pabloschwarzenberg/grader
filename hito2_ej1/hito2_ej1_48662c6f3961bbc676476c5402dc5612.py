adn1 = list(input())
adn2 = list(input())
alineamiento = []
i = 0
j = 0
while i < len(adn2) and j < len(adn1):
    if adn2[i] == adn1[j]:
        alineamiento.append(adn2[i])
        i += 1
        j += 1
    else:
        alineamiento.append('_')
        j += 1

while i < len(adn2):
    alineamiento.append(adn2[i])
    i += 1

string = ''.join(alineamiento)
print(string)