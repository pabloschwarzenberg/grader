class JuegoDelGato:
    def __init__(self):
        self.tablero=[[0,0,0],              
                      [0,0,0],
                      [0,0,0]]
    
    def jugarGato(self,fila,columna):               
        if (self.tablero[fila][columna]==0):        
            self.tablero[fila][columna]=1           
            return True
        else:
            return False
            
    def jugarRaton(self):
        fila=0                                  
        max1=0
        verif=0
        for i in range(3):                          
            cont=0                                                      
            for j in range(3):                      
                if(self.tablero[i-1][j-1]==1):          
                    if(cont>max1 and cont<3):
                        fila=i-1
                        max1=cont                           
                if(self.tablero[i-1][j-1]==0):          
                    verif=1     
        columna=0
        max2=0
        for i in range(3):
            cont=0
            for j in range(3):
                if(self.tablero[j-1][i-1]==1):
                    cont=cont+1
                    if(cont>max1 ):
                        columna=i-1
                        max2=cont                          
        
        if(max2==3 or max1==3):          
            return False
 
        if((self.tablero[0][0]==1 and self.tablero[1][1]==1) or (self.tablero[0][0]==1 and self.tablero[2][2]==1)or (self.tablero[1][1]==1 and self.tablero[2][2]==1)):
            for i in range(3):
                if(self.tablero[i-1][i-1]==0):
                    self.tablero[i-1][i-1]=-1
                    return True
        elif((self.tablero[0][2]==1 and self.tablero[1][1]==1) or (self.tablero[0][2]==1 and self.tablero[2][0]==1)or (self.tablero[1][1]==1 and self.tablero[2][0]==1)):
            if(self.tablero[0][2]==0):
                self.tablero=-1
                return True
            elif(self.tablero[1][1]==0):
                self.tablero=-1
                return True
            elif(self.tablero[2][0]==0):
                self.tablero=-1
                return True
        if(max1==0 and max2==0):
            self.tablero[1][1]=-1
            return True
        if(max1>=max2):
            for i in range(3):
                if(self.tablero[columna][i-1]==0):
                    self.tablero[columna][i-1]=-1
                    return True
        else:
            for i in range(3):
                if(self.tablero[i-1][fila]==0):
                    self.tablero[i-1][fila]=-1
                    return True 
                
    def mostrar_tablero(self):
        print(str(self.tablero[0][0])+" | "+str(self.tablero[0][1])+" | "+str(self.tablero[0][2]))
        print("-----------")
        print(str(self.tablero[1][0])+" | "+str(self.tablero[1][1])+" | "+str(self.tablero[1][2]))
        print("-----------")
        print(str(self.tablero[2][0])+" | "+str(self.tablero[2][1])+" | "+str(self.tablero[2][2]))
                    
    def cargar_tablero(self,matriz):
        for i in range(3):
            for j in range(3):
                self.tablero[i][j]=matriz[i][j]
    
    def indicar_estado(self):
        cont=0
        cont2=0
        validador=0
        for i in range(3):
            cont=0
            for j in range(3):
                if(self.tablero[i-1][j-1]==1):
                    cont=cont+1                         
                elif(self.tablero[i-1][j-1]==-1):          
                    cont2=cont2+1
                elif(self.tablero[i-1][j-1]==0):            
                    validador=1
        if(cont==3):
            return(2)
        elif(cont2==3):
            return(3)
        elif(self.tablero[0][0]==1 and self.tablero[1][1]==1 and self.tablero[2][2]==1):           
            return(2)
        elif(self.tablero[0][0]==-1 and self.tablero[1][1]==-1 and self.tablero[2][2]==-1):        
            return(3)
        elif(self.tablero[0][2]==1 and self.tablero[1][1]==1 and self.tablero[2][0]==1):            
            return(2)
        elif(self.tablero[0][2]==-1 and self.tablero[1][1]==-1 and self.tablero[2][0]==-1):       
            return(3)   
        elif(validador==1):                                                                                   
            return(0)
        else:
            return(1)                                   
        
        
            
if __name__ == "__main__":

    juego1= JuegoDelGato()
    juego1.mostrar_tablero()
    print(juego1.indicar_estado())
    juego1.jugarGato(1,1)
    juego1.mostrar_tablero()
    print(juego1.indicar_estado())
    juego1.jugarRaton()
    juego1.mostrar_tablero()
    print(juego1.indicar_estado())
    juego1.jugarRaton()
    juego1.mostrar_tablero()
    print(juego1.indicar_estado())
    juego1.jugarRaton()
    juego1.mostrar_tablero()
    print(juego1.indicar_estado())
    juego1.jugarRaton()
    juego1.mostrar_tablero()
    print(juego1.indicar_estado())