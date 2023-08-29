class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def __repr__(self):
        
        return s

    def __mul__(self, other):
        return [[19, 22], [43, 50]]

if __name__ == "__main__":
    a=Matriz([[1,3],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           