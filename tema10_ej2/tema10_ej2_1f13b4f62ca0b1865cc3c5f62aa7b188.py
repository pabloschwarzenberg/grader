#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    
    lev_dist = ''
    p1 = list(palabra1)
    p2 = list(palabra2)

    if palabra2 == palabra1: 
        lev_dist = '0D'

    elif len(palabra1) == len(palabra2): 
        dis_s = 0 
        for pos in range(len(palabra1)): 
            if p1[pos] != p2[pos]: 
                dis_s = dis_s +1 
            if dis_s > 1: 
                lev_dist = '+1'
                break
        else: 
            if dis_s == 1: 
                lev_dist = '1S'
    
    else: 
        dis_ib = abs(len(palabra1) - len(palabra2))
        dis_ibs  = 0
        for pos in range(min(len(palabra1), len(palabra2))): 
            if p1[pos] not in p2: 
                dis_ibs = dis_ibs +1 
            if dis_ibs > 1: 
                lev_dist = '+1'
                break
#########
        if (dis_ib == 1) and (dis_ibs == 0): 
            lev_dist = 'IB'
        elif (dis_ib == 0) and (dis_ibs == 1): 
            lev_dist = '1S'
        elif (dis_ib+ dis_ibs) > 1: 
            lev_dist = '+1'
    
    return lev_dist


if __name__=="__main__":
    
    print(
        levenshtein(
            'jarron', 
            'melon'
        )
    )
           