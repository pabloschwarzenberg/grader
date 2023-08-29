def jerigonzo(string):
    
    traduccion_propuesta = []
    
    for palabra in string:
        
        for vocal in palabra:
            
            if vocal in "aeiouAEIOU":
                vocal = vocal + "p"+ vocal
            traduccion_propuesta.append(vocal)
    traduccion_propuesta = "".join(traduccion_propuesta)
    
    return traduccion_propuesta