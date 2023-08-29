def numero_perfecto(a):
    def findDiv(a):
        divis = []
        for div in range(1,a):
            if (a%div) == 0:
                divis.append(div)
        return divis
    
    divSum =  sum(findDiv(a))
    if divSum == a:
        return True
    elif divSum != a:
        return False
        
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
           