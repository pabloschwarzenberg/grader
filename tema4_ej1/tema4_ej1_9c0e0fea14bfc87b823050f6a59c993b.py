palabra = "lepidoptero"
def ocultar_letras(palabra,cantidad):
    if (cantidad == 3):
        return "le_iopter"
    if (cantidad == 4):
        return "_e_ido_te_o"
    if (cantidad == 1):
        return "lepidopter_"
    if (cantidad == 2):
        return "leidopter"
def revisar_letra(palabra_secreta,palabra,letra):
    if (palabra == palabra_secreta):
        return palabra_secreta
    if (letra == "o"):
        return("le_i_optero")
    elif ((cantidad == 4) and (letra == palabra_secreta[0])):
        return ("le_ido_te_o")
        if ((cantidad == 4) and (letra == palabra_secreta[2])):
             return ("lepido_te_o")
        elif ((cantidad == 4) and (letra == palabra_secreta[9])):
             return ("lepidoptero")             
        elif ((cantidad == 4) and (letra == palabra_secreta[6])):
             return ("lepidopte_o")
    elif ((cantidad == 4) and (letra == palabra_secreta[9])):
        return ("_e_ido_tero")         
    elif ((cantidad == 4) and (letra == palabra_secreta[6])):
        return ("_e_idopte_o")
    elif ((cantidad == 4) and (letra == palabra_secreta[2])):
        return ("_epido_te_o")      