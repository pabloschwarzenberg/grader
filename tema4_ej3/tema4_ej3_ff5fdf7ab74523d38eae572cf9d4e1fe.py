def jerigonzo(palabra):
    palabrafinal=''

    for letra in palabra:
        if letra== "a":
            palabrafinal=palabrafinal+letra+'pa'          
        elif letra== "e":
            palabrafinal=palabrafinal+letra+'pe'
        elif letra== "i":
            palabrafinal=palabrafinal+letra+'pi'
        elif letra== "o":
            palabrafinal=palabrafinal+letra+'po'
        elif letra== "u":
            palabrafinal=palabrafinal+letra+'pu'
        else:
            palabrafinal=palabrafinal+letra
        
    return palabrafinal


if __name__ == "__main__":
    pass
         