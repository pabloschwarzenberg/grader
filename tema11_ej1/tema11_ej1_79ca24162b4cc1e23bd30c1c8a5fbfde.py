def palindromo(palabra):
    if len(palabra)==0:
        return True
    if len(palabra)==1:
        return True
    else:
        cabeza=palabra[0]
        cuerpo=palabra[1:len(palabra)-1]
        cola=palabra[len(palabra)-1]
        cuerpo_palindromo=palindromo(cuerpo)
        if cuerpo_palindromo and (cabeza==cola):
            return True
        else:
            return False