letra=[]
b=''
def buscarTodas(a,b):
    x = b
    letra = [idx for idx, b in enumerate(a) if b==x]
    return " ".join(map(str,letra))
    pass

if __name__ == "__main__":
    
    
    pass