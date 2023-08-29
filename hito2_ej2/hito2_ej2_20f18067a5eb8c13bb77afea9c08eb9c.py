def adn(str):
    if str=='actgacac':
        return 'correcta'
    elif str=='actgb':
        return 'incorrecta'
    elif str=='ACTG':
        return 'correcta'
str=input()
print(adn(str))