#Completa el ejemplo de la clase Matriz agregando un método __mul__ que permita multiplicar dos matrices.


class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
        a = self.celdas[0][0]* other.celdas[0][0] + self.celdas[0][1]* other.celdas[1][0]
        b = self.celdas[1][0]* other.celdas[0][0] + self.celdas[1][1]* other.celdas[1][0]
        c = self.celdas[0][0]* other.celdas[0][1] + self.celdas[0][1]* other.celdas[1][1]
        d = self.celdas[1][0]* other.celdas[0][1] + self.celdas[1][1]* other.celdas[1][1]
        A = Matriz([[a,c],[b,d]]) 
        
        return A

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           
           