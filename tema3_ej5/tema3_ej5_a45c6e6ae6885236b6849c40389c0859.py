class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def camino(self,Ciudad):                #p1= 1,0, -> p2=3,3
        x=self.x                            #p1.camino(p2), x.self=1 -> y.self=0
        y=self.y
        x2=Ciudad.x                         #p2.x = 3 , p2.y = 3
        y2=Ciudad.y
        camino=[[x,y]]                      #camino=[1,1],
        while(x!=x2 or y!=y2):              
            #print(x,x2,y,y2)
            if (x>x2 and y>y2):             #1>3 y 0>3, 
                camino.append([x-1,y-1])                
                x=x-1
                y=y-1
            elif x>x2 and y==y2:
                camino.append([x-1,y])
                x=x-1
            elif x>x2 and y<y2:
                camino.append([x-1,y+1])
                x=x-1
                y=y+1
            elif x==x2 and y>y2:
                camino.append([x,y-1])
                y=y-1
            elif x==x2 and y<y2:
                camino.append([x,y+1])
                y=y+1
            elif x<x2 and y>y2:
                camino.append([x+1,y-1])
                x=x+1
                y=y-1
            elif x<x2 and y<y2:                 #  1<3 y 0<3, (1,0)->(2,1)
                camino.append([x+1,y+1])        #  
                x=x+1
                y=y+1
            elif x<x2 and y==y2:
                camino.append([x+1,y])            
                x=x+1
                y=y
        return(camino)
    def distancia(self,ciudad):
        distancias=0
        caminos=(self.camino(ciudad))
        tamano=(len(caminos))-1
        contador=0
        while(tamano-1>contador):
            distancias=distancias+((((caminos[contador+1][0])-caminos[contador][0])**2)+(((caminos[contador+1][1])-caminos[contador][1])**2))**(0.5)*(2)
            contador=contador+1
        return distancias
        
    
if __name__ == "__main__":

    p1=Ciudad(1,1)     #self.x=1, self.y=0
    p2=Ciudad(3,3)      #self.x=3, self.y=3
    print("hola.2")
    print(p1.camino(p2))        #1,0 -> 3,3 
    print(p1.distancia(p2))

#clase ciudad (x,y):
#   
#   self.x=x
#metodos camino y distancia
         