adn = input()
n = int(input())

for i in range(len(adn) - n + 1):
    if adn.count(adn[i: i + n]) == 1:
        print(adn[i: i + n])
else:
    print('ninguna')