def validarsecuencia(secuencia):
    proteinas=["A","T","C","G"]
    sec=list(secuencia.upper())
    k=0
    result=""
    while k<len(sec):
        if sec[k] not in proteinas:
            result="no"
        k=k+1
    if result=="no":
        return("La secuencia %s es incorrecta"%(secuencia))
    else:
        return("La secuencia %s es correcta"%(secuencia))
secuencia=input()
print(validarsecuencia(secuencia))
    
