# por favor escribe aquí tu función
def es_primo(n):
    if n==1 or n==4 or n==6 or n==8 or n==9:
        return False
    elif n==2 or n==3 or n==5 or n==7:
        return True
    elif  n%2!=0 and n%3!=0 and n%4!=0 and n%5!=0 and n%6!=0 and n%7!=0 and n%8!=0 and n%9!=0:
        return True
    else:
        return False   