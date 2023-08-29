def numero_perfecto(n):
            sumatoria=0
            lista=[]
            for i in range(1,n):
                if n%i==0:
                    sumatoria=sumatoria+i
                    lista.append(i)


                        
                
            if sumatoria==n:
                return True 


            else:
                return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))