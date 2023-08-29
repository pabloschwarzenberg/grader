def validar_adn(psec): # Posible secuencia
    admit = 'ACTG'
    inc = 0
    for i in psec:
        if i.upper() not in admit:
            inc += 1
    
    if inc != 0:
        print('SECUENCIA INCORRECTA')
    
    else:
        print('SECUENCIA CORRECTA')
        
in_sec = input()
validar_adn(in_sec)