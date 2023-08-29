def levenshtein(palabra1,palabra2):
    d=(len(palabra2)-len(palabra1))
    d = d if d > 0 else (d*-1)
    if d>1:
        distancia='+1'
    elif d==1 and (len(palabra1)!=len(palabra2)):
        distancia='IB'
    elif d==1 and (len(palabra1)==len(palabra2)):
        distancia='1S'
    elif d==0:
        for i in range(len(palabra1)):
            if palabra1[i] != palabra2[i]:
                return '1S'
        distancia='0D'
    return distancia

if __name__=="__main__":
    d=levenshtein("hola","ola")
    print(d)
