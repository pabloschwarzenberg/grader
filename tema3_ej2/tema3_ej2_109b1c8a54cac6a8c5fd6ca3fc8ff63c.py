class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        x=(self.x)**2
        y=(self.y)**2
        z=(self.z)**2
        norma=(x+y+z)**(1/2)
        print(x,y,z)
        return norma

    def suma_vectores(self,other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.z+other.z
        vector=Vector(x,y,z)
        return vector

    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.z+other.z
        vector=Vector(x,y,z)
        return vector

    def __str__(self):
        return str(self.x)+","+str(self.y)+","+str(self.z)