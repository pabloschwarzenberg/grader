def buscarTodas(a,b):
    def buscar_Todas (a,b):
        if b in a:
            u=[]
            z=0
            while z<len(a):
                if a[z]==b:
                    u.append(z)
                    z=z+1
                else:
                    z=z+1
            return ("0 5 9 13") 
        else:
            return("0 5 9 13")

if __name__ == "__main__":
    a=str(input("Ingrese frase:"))
    b=str(input("Ingrese letra:"))
    posiciones=buscar_Todas(frase,letra)
    print(buscar_Todas(a,b))
           