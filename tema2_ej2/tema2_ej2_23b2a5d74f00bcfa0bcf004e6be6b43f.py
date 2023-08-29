# completa el código de la función
def amigos(a,b):
    suma1 = 0
    suma2 = 0
    if a == b:
        return False
    else:
        div1 = round(a/b, 1)
        div1 = str(div1)
        concatena1 = div1.replace(".", "") 
        concatena1 = list(map(int, concatena1))
        suma1 = sum(concatena1)

        div2 = round(b/a, 1)
        div2 = str(div2)
        concatena2 = div2.replace(".", "") 
        concatena2 = list(map(int, concatena2))
        suma2 = sum(concatena2)
        if suma1 == suma2:
            return True
        else:
            return False
           