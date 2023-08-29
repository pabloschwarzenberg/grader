def jerigonzo(y):
    palabra_nueva=""
    for i in y:
        palabra_nueva+=i
        if i=="a":
            palabra_nueva+="pa"
        if i=="e":
            palabra_nueva+="pe"
        if i=="i":
            palabra_nueva+="pi"
        if i=="o":
            palabra_nueva+="po"
        if i=="u":
            palabra_nueva+="pu"
    return palabra_nueva
if __name__ == "__main__":
    pass
         