import random
l=["lepidoptero","bebida","correo","esponja","almacen","pajaros"]
p_sec=random.choice(l)

def ocultar_letras(p_sec,cant):
    st=""
    l=[]
    while len(l)<cant:
        r=random.randint(0,len(p_sec)-1)
        if not(r in l):
            l.append(r)
    for i in range(len(p_sec)):
        if i in l:
            st+="_"
        else:
            st+=p_sec[i]
    return(st)
                   


            
        
        

def revisar_letra(sec,sec_,letra):    
    st=""                   
    if letra==sec:
        return(sec)
    for i in range(len(sec_)):
        if sec_[i]==sec[i]:
            st+=sec[i]
        else:
            if sec[i]==letra:
                st+=letra
            else:
                st+="_"
    return(st)
        
                

if __name__ == "__main__":
    pass
         