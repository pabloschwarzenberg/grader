class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas
    def __multi__(self,a=[],b=[]):
        x=a[0][0]*b[0][0] + a[0][1]*b[1][0] 
        y=a[0][0]*b[0][1] + a[0][1]*b[1][1]
    
        x1=a[1][0]*b[0][0] + a[1][1]*b[1][0] 
        y1=a[1][0]*b[0][1] + a[1][1]*b[1][1]
        
        return [[x,y],[x1,y1]]
           