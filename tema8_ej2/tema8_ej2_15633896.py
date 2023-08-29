posiciones=""
def buscarTodas(a,b):

    c=len(a)
    

    for i in range(0,c):
        if b==(a[i]):
            d=str(i)
            if i==0:
                posiciones=d
            else:posiciones=posiciones+" "+d

    return posiciones
            
if __name__ == "__main__":
    pass
           