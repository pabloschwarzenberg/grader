#funcion suma divisores de un numero
def suma_divisores(a):
    divi = [1]
    for i in range (2, a + 1):
        if a % i == 0:
             divi.append(i)
    divi.remove(a)
    
    if sum(divi) == 1:
        Primo = True
        return (sum(divi), Primo)
    else:
        Primo = False
        return (sum(divi), Primo)
