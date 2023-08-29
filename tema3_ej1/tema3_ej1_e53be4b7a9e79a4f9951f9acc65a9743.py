# completa el código de la función
def suma_divisores(a):
        Lista_divisores = []
        for i in range(1, a):
            if a % i == 0:
                Lista_divisores.append(i)
        sumadiv = int(sum(Lista_divisores))
        if sumadiv == 1:
            x = True
        else:
            x = False
        return sumadiv, x
 
           