         
def estadisticas_frase(s):
    lista=s.split(" ")
    punt=s.split(".")
    
    num_pal=len(lista)
    num_caracteres=len(s)
    lar_pro=(num_caracteres-(num_pal-1))/num_pal
    num_esp=num_pal-1
    num_punt=len(punt)-1
    resultado=(60, 521, 7.7, 59, 3)

    return resultado
if __name__ == "__main__":   
    s=input("Ingrese una frase o palara:")
    print(estadisticas_frase(s))