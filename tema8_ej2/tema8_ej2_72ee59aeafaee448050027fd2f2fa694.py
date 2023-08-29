if __name__ == "__main__":
  a = input("ingrese frase")
  b = input("ingrese letra")

a = ""
b = ""
def buscarTodas(a,b):
    
    a = list(a)
    y = ""
    i=0
    while b in a:
        
        x = a.index(b)
        y = y+str(x)+" "
        a[x] = "0"
        i+=1
        y[:len(y)-2]
    return y.strip()
        
buscar = buscarTodas(a,b)
print(buscar)


    
           