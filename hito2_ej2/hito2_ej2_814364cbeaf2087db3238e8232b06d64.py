def validar_secuencia_adn(secuencia):
    
    secuencia = secuencia.upper()
    
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False
    
  
    return True


secuencia = input('Ingresa la secuencia de ADN: ')


if validar_secuencia_adn(secuencia):
    print('secuencia correcta')
else:
    print('secuencia incorrecta')
