import math
class Ciudad:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def distancia(self,p2):
        x_2 = self.x-p2.x
        y_2 = self.y-p2.y
        return math.sqrt((x_2**2)+(y_2**2))
    def camino(self, p2):
        x_c = 0
        y_c = 0
        m = 0
        result = []
        if self.x >= p2.x:
            result = [[int(p2.x),int(p2.y)]]
            m=(p2.y-self.y)/(p2.x-self.x)
            x_c = p2.x
            y_c = p2.y
            while x_c != self.x and y_c != self.y:
                if x_c!= self.x:
                    x_c += m
                if y_c != self.y:
                    y_c += (1/m)
                result.append([int(x_c),int(y_c)])
        if p2.x > self.x:
            result = [[int(self.x), int(self.y)]]
            m=(self.y-p2.y)/(self.x-p2.x)
            x_c = self.x
            y_c = self.y
            while x_c != p2.x and y_c != p2.y:
                if x_c!= p2.x:
                    x_c+=m
                if y_c != p2.y:
                    y_c+=(1/m)
                result.append([int(x_c),int(y_c)])
        return result

if __name__ == "__main__":
  pass
         