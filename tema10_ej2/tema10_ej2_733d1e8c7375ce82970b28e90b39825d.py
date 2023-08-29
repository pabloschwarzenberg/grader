#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if len(palabra1)==len(palabra2):
        if palabra1==palabra2:
            return "0D"
        else:
            pLarga=palabra1
            pCorta=palabra2
    if len(palabra1) > len(palabra2):
        pLarga=palabra1
        pCorta=palabra2
    elif len(palabra1) < len(palabra2):
        pLarga=palabra2
        pCorta=palabra1
    for letra in pLarga:
        if letra in pCorta:
            pLarga=pLarga.replace(letra,"*",1)
            pCorta=pCorta.replace(letra,"*",1)
    sobranteL=[]
    sobranteC=[]
    for caracter in pLarga:
        if caracter.isalpha()==True:
            sobranteL.append(caracter)
    for caracter in pCorta:
        if caracter.isalpha()==True:
            sobranteC.append(caracter)
    if  len(sobranteL)>1:
        return "+1"
    elif    len(sobranteL)==1 and len(sobranteC)==0:
        return "IB"
    elif    len(sobranteL)==1 and len(sobranteC)==1:
        return "1S"
        
if __name__=="__main__":
    p_1=input("Ingrese palabra 1: ")
    p_2=input("Ingrese palabra 2: ")
    print(levenshtein(p_1,p_2))