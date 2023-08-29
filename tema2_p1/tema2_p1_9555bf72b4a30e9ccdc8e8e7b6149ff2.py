def es_primo(p):
    if p<=1:
        print("No Valido")
        return False
    else:
        for i in range(2,p):
            a=p/i
            if a==int(a):
                print("No es Primo")
                return False
        print("Es Primo")
        return True