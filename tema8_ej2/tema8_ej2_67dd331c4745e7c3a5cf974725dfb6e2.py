#Debe mostrar donde sse encuentra la letra b en el string a
# por ejemplo, en "tres tristes tigres"
# la t se encuentra en '0,5,9,13'
# esto se debe mostrar en pantalla
# (los espacios deben contar como string)
letras=[]
b=''
def buscarTodas(a,b):
    x = b
    letras = [idx for idx, b in enumerate(a) if b==x]
    return " ".join(map(str,letras))
    pass

if __name__ == "__main__":
    
    
    pass
           