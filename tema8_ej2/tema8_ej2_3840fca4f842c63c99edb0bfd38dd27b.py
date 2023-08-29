letras=[]
b=''
def buscarTodas(a,b):
    x = b
    letras = [idx for idx, b in enumerate(a) if b==x]
    return " ".join(map(str,letras))
    pass

if __name__ == "__main__":
    
    
    pass  