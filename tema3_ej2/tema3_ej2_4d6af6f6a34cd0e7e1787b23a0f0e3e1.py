class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        norm=(((self.x)**2)+((self.y)**2)+((self.z)**2))**(1/2)
        return (norm)
    def suma_vectores(self,v1,v2):
        self.vectorf=operator.add(v1,v2)
        return self.vectorf     
        
if __name__ == "__main__":
   v1=Vector(1,2,3)
 