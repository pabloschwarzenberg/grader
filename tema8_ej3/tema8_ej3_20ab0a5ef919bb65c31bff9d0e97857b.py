#El antipoema
def estadisticas_frase(s):
    b=s.split()
    pro_largo=0    
    contar_caracteres=0
    contar_palabras=0
    largo_palabra=0
    contar_espacios=0
    contar_puntuacion=0  
    
    for i in s:
        contar_caracteres=contar_caracteres+1
    
    for i in b:
        contar_palabras=contar_palabras+1
        largo_palabra=largo_palabra + len(i)
 
    for i in range(len(s)):
        if(ord(s[i])==32):
            contar_espacios=contar_espacios+1
  
    for i in range(len(s)):
        if( ord(s[i])!=32 and ord(s[i])!=10   and 
          ( ord(s[i])<97  or  ord(s[i])>122 ) and 
          ( ord(s[i])<65  or  ord(s[i])>90  ) and 
          s[i]!="á" and s[i]!="é" and s[i]!="í" and s[i]!="ó" and s[i]!="ú" and
          s[i]!="Á" and s[i]!="É" and s[i]!="Í" and s[i]!="Ó" and s[i]!="Ú" ):
            contar_puntuacion=contar_puntuacion+1

    pro_largo = (largo_palabra-contar_puntuacion)/contar_palabras 

    return contar_palabras,contar_caracteres,pro_largo,contar_espacios,contar_puntuacion