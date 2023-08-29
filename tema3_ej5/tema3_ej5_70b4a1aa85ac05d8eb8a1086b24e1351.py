class Ciudad:
    def __init__(self,vector_x,vector_y):
        self.vector_x = vector_x
        self.vector_y = vector_y

    def camino(self, Ciudad):
        trayecto = [[self.vector_x, self.vector_y]]
        while (trayecto[-1] != [Ciudad.vector_x,Ciudad.vector_y]):
            if (self.vector_x < Ciudad.vector_x):
                if (self.vector_y < Ciudad.vector_y):
                    
                    trayecto.append([trayecto[-1][0] + 1, trayecto[-1][1] + 1])
                else:
                       
                    trayecto.append([trayecto[-1][0]+ 1, trayecto[-1][1]])

            elif (self.vector_x > Ciudad.vector_x and self.vector_y < Ciudad.vector_y):
                
                trayecto.append([trayecto[-1][0], trayecto[-1][1]+ 1])
            
            elif (self.vector_x > Ciudad.vector_x):

                if (self.vector_y > Ciudad.vector_y):
                    
                    trayecto.append([trayecto[-1][0] -1, trayecto[-1][1] - 1])
                else:    
                    
                    trayecto.append([trayecto[-1][0] - 1, trayecto[-1][0]])

            elif (self.vector_x < Ciudad.vector_x and self.vector_y > Ciudad.vector_y):
                
                trayecto.append([trayecto[-1][0], trayecto[-1][1]- 1])
        return trayecto


    def distancia(self, Ciudad):
        math1 = (Ciudad.vector_x-self.vector_x)**2
        math2 = (Ciudad.vector_y-self.vector_y)**2
        return (math1+math2)**0.5


        
if __name__ == "__main__":
  pass
         