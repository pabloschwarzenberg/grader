def is_adn(st):
    no = 'bdefhijklmnopqrsuvwxyz'
    is_adn = True
    for i in adn:
        if i in no:
            is_adn = False
            break
    return is_adn

adn = input()

if is_adn(adn) == True:
    print('secuencia correcta')
else:
    print('secuencia incorrecta')