# completa el código de la función
def suma_divisores(n):

    div = [1]

    for i in range(2,n+1):
    
        if n%i ==0:
        
            div.append(i)

    if sum(div) %2:
    
        return sum(div)-n, False
        
    else:
    
        return sum(div)-n, True


print(suma_divisores(1))