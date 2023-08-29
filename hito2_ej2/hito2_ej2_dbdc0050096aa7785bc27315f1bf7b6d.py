def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()
    secuencia = list(secuencia)
    genoma = ['A','C','T','G']
    for i in secuencia:
        if i in genoma :
            a = True 
        elif i not in genoma:
            a = False 
            break
    if a == True:
        return 'Secuencia correcta'
    elif a == False:
        return 'Secuencia incorrecta'
           
                

        
z = input('secuencia: ')            
    
print(validar_secuencia_genoma(z))
           
                