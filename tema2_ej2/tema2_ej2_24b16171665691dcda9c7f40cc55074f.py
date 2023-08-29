# completa el código de la función
def amigos(a,b):
    divisores_de_a = 1
    divisores_de_b = 1
    
    for valores in range(2,a):
        if a % valores == 0 :
            divisores_de_a = divisores_de_a + valores
            
    for valor in range(2,b):
        if b % valor == 0 :
            divisores_de_b = divisores_de_b + valor
            
    if a==2 or b==2:
    
        if a==2:
            divisores_de_a = divisores_de_a + 2
            
        if b==2:
            divisores_de_b = divisores_de_b + 2
            
    if divisores_de_a == b or divisores_de_b == a :
        return (True)
        
    else:
        return(False)
