tipo_adn = ['A','C','G','T']
adn = str(input('Ingrese el adn: '))
adn = adn.upper()
print(adn)
adn_v = False
adn_in = False
for i in adn:
    if i in tipo_adn:
        adn_v = True
    else: 
        adn_in = True
        adn_v = False

    
if adn_v == True:
    print('secuencia correcta')

if adn_in == True:
    print('secuencia incorrecta')