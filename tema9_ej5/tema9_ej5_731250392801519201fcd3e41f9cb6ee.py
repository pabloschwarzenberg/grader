import random
class JuegoDelGato:
    def __init__(self):
        self.tab=[[0,0,0],[0,0,0],[0,0,0]]
        self.bol2=True
        self.state=0
    def jugarGato(self,fila,columna):
        if self.tab[fila][columna]==0:
            self.tab[fila][columna]=1
            return True
        else:
            return False
    def jugarRaton(self):
        tau=True
        for i in range(0,3):#se revisan verticalmente
            s=""
            for j in range(0,3):
                s+=str(self.tab[j][i])
            if s=="0-1-1":
                tau=False
                self.tab[0][i]=-1
            elif s=="-10-1":
                tau=False
                self.tab[1][i]=-1
            elif s=="-1-10":
                tau=False
                self.tab[2][i]=-1                
            elif s=="011":
                tau=False
                self.tab[0][i]=-1
            elif s=="101":
                tau=False
                self.tab[1][i]=-1
            elif s=="110":
                tau=False
                self.tab[2][i]=-1
        if tau:
            for i in range(0,3):#se revisan horizontalmente               
                s=""                
                for j in range(0,3):                    
                    s+=str(self.tab[i][j])
                if s=="0-1-1":
                    tau=False
                    
                    self.tab[i][0]=-1
                elif s=="-10-1":
                    tau=False
                    self.tab[i][1]=-1
                elif s=="-1-10":
                    tau=False
                    self.tab[i][2]=-1
                elif s=="011":
                    tau=False
                    self.tab[i][0]=-1
                elif s=="101":
                    tau=False
                    self.tab[i][1]=-1
                elif s=="110":
                    tau=False
                    self.tab[i][2]=-1
        if tau:
            if str(self.tab[0][0])+str(self.tab[1][1])+str(self.tab[2][2])=="0-1-1":
                tau=False
                self.tab[0][0]=-1
            elif str(self.tab[0][0])+str(self.tab[1][1])+str(self.tab[2][2])=="-10-1":
                tau=False
                self.tab[1][1]=-1
            elif str(self.tab[0][0])+str(self.tab[1][1])+str(self.tab[2][2])=="-1-10":
                tau=False
                self.tab[2][2]=-1               
            elif str(self.tab[0][2])+str(self.tab[1][1])+str(self.tab[2][0])=="0-1-1":#####
                tau=False
                self.tab[0][2]=-1
            elif str(self.tab[0][2])+str(self.tab[1][1])+str(self.tab[2][0])=="-10-1":
                tau=False
                self.tab[1][1]=-1
            elif str(self.tab[0][2])+str(self.tab[1][1])+str(self.tab[2][0])=="-1-10":
                tau=False
                self.tab[2][0]=-1

                
            elif str(self.tab[0][0])+str(self.tab[1][1])+str(self.tab[2][2])=="011":
                tau=False
                self.tab[0][0]=1
            elif str(self.tab[0][0])+str(self.tab[1][1])+str(self.tab[2][2])=="101":
                tau=False
                self.tab[1][1]=1
            elif str(self.tab[0][0])+str(self.tab[1][1])+str(self.tab[2][2])=="110":
                tau=False
                self.tab[2][2]=1                            
            elif str(self.tab[0][2])+str(self.tab[1][1])+str(self.tab[2][0])=="011":#####
                tau=False
                self.tab[0][2]=1
            elif str(self.tab[0][2])+str(self.tab[1][1])+str(self.tab[2][0])=="101":
                tau=False
                self.tab[1][1]=1
            elif str(self.tab[0][2])+str(self.tab[1][1])+str(self.tab[2][0])=="110":
                tau=False
                self.tab[2][0]=1
        if tau:
            bol=True
            while bol:
                
                j1=random.randint(0,2)
                j2=random.randint(0,2)
                if self.tab[j1][j2]==0:
                    self.tab[j1][j2]=-1
                    bol=False                            
    def mostrar_tablero(self):
        return(self.tab)
    def cargar_tablero(self,matriz):
        self.tab=matriz
    def indicarEstado(self):
        if self.bol2:
            for i in range(0,3):#se revisan verticalmente
                
                s=""
                for j in range(0,3):
                    s+=str(self.tab[j][i])
                if s=="-1-1-1":
                    self.state=3
                    self.bol2=False

                    
            for i in range(0,3):#se revisan horizontalmente               
                s=""                
                for j in range(0,3):                    
                    s+=str(self.tab[i][j])
                if s=="-1-1-1":
                    self.state=3
                    self.bol2=False
            for i in range(0,3):#se revisan verticalmente
                
                s=""
                for j in range(0,3):
                    s+=str(self.tab[j][i])
                if s=="111":
                    self.state=2
                    self.bol2=False

                    
            for i in range(0,3):#se revisan horizontalmente               
                s=""                
                for j in range(0,3):                    
                    s+=str(self.tab[i][j])
                if s=="111":
                    self.state=2
                    self.bol2=False


                
            if str(self.tab[0][0])+str(self.tab[1][1])+str(self.tab[2][2])=="111":
                self.state=2
                self.bol2=False
            if str(self.tab[0][2])+str(self.tab[1][1])+str(self.tab[2][0])=="111":
                self.state=2
                self.bol2=False
            if str(self.tab[0][0])+str(self.tab[1][1])+str(self.tab[2][2])=="-1-1-1":
                self.state=3
                self.bol2=False
            if str(self.tab[0][2])+str(self.tab[1][1])+str(self.tab[2][0])=="-1-1-1":
                self.state=3
                self.bol2=False                    
            return self.state       
        if self.bol2:
            s=9
            c=0
            for i3 in self.tab:
                for j3 in i:
                    if j3 ==1 or j3==-1:
                        c+=1
            if s==c:
                return 1
            else:
                return 0                    
        else:
            return self.state
            
        
                
        

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         