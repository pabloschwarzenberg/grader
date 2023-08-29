def palindromo(palabra):
    if palabra=="":
        return True
    else:
        if palabra[0]!=palabra[-1]:
            return False
        else:
            return palindromo(palabra[1:-1])
            

           