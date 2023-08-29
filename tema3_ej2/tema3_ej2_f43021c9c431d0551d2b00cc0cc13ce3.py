class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        n=(self.x**2+slef.y**2+self.z**2)**1/2
        return n

    def __add__(self,other):
        a=self.x+other.x
        b=self.y+other.y
        c=self.z+other.z
        return vector(a,b,c)

    def __str__(self):
        return("x={0}, y={1}, z={2}".format(self.x,self.y,self.z))
        


def suma_vectores(a1,a2):
    n=a1+a2
    return n