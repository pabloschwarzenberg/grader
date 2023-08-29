class Matriz:
    def __init__(self, celdas = []):
        self.celdas = celdas
    
    def __repr__(self):
        s = ""
        
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s += "{0: >5} ".format(self.celdas[i][j])
            
            s += "\n"
        return s
    
    def __mul__(self, other):
        mat = Matriz([])
        
        mat = Matriz([[self.celdas[0][0] * other.celdas[0][0] + self.celdas[0][1] * other.celdas[1][0], self.celdas[0][0] * other.celdas[0][1] + self.celdas[0][1] * other.celdas[1][1]], [self.celdas[1][0] * other.celdas[0][0] + self.celdas[1][1] * other.celdas[1][0], self.celdas[1][0] * other.celdas[0][1] + self.celdas[1][1] * other.celdas[1][1]]])
        
        return mat

if __name__ == "__main__":
    matriz_a = Matriz([[1,2],[3,4]])
    
    matriz_b = Matriz([[5,6],[7,8]])
    
    res = matriz_a * matriz_b
    
    print(res)