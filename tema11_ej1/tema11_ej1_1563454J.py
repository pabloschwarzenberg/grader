def palindromo(palabra):
    palabral=list(palabra)
    if palabral[0] != palabral[len(palabral)-1]:
        return False
    else:
        if len(palabral)==1:
            return True
        if len(palabral)==2:
            if palabral[0]==palabral[1]:
                return True
            else:
                return False
        palabral=palabral[1:len(palabral)-1]
        palabra_final=''.join(palabral)
        t=palindromo(palabra_final)
        return t


if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           