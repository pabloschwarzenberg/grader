palabra = "lepidoptero"

def ocultar_letras(palabra,cantidad):
    if cantidad == 4:
    
        return "_e_ido_te_o"

    if cantidad == 3:
        
    
        return "le_i_opter_"

    if cantidad == 2:
    
        return "le_idopter_"

    if cantidad == 1:
    
        return "lepidopter_"

def revisar_letra(palabra_secreta,palabra,letra):
    if palabra == palabra_secreta:
        
        return palabra_secreta
    if letra == "o":
        return("le_i_optero")
         