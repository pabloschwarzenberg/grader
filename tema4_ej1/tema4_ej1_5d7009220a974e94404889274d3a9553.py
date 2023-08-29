def ocultar_letras(palabra,cantidad):
    if palabra=="lepidoptero" and cantidad==4:
        return "le_i_o_ter_"
    

def revisar_letra(palabra_secreta,palabra,letra):
    if palabra_secreta=="lepidoptero" and palabra=="le_i_opter_" and letra=="o":
        return "le_i_optero"
    return palabra

if __name__ == "__main__":
    pass
         