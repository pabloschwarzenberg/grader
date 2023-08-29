class Ciudad:

    def __init__(self,px,py):
            self.px=px
            self.py=py
    def camino(self,other):
        
        c1=[self.px,self.py]
        c2=[other.px,other.py]
        pasos = []
        if c1[0] >= c2[0] and c1[1] >= c2[1]:
            p = ["", ""]
            i = 0
            while p[0] != c2[0] and p[1] != c2[1]:
                p[0] = c1[0] - i
                p[1] = c1[1] - i
                pp = [p[0], p[1]]
                pasos.append(pp)
                i += 1
            if p[0] > c2[0]:
                while p[0] > c2[0]:
                    p[0] = p[0] - 1
                    pp = [p[0], p[1]]
                    pasos.append(pp)
        if c1[0] >= c2[0] and c1[1] <= c2[1]:
            p = ["", ""]
            i = 0
            while p[0] != c2[0] and p[1] != c2[1]:
                p[0] = c1[0] - i
                p[1] = c1[1] + i
                pp = [p[0], p[1]]
                pasos.append(pp)
                i += 1
            if p[0] > c2[0]:
                while p[0] > c2[0]:
                    p[0] = p[0] - 1
                    pp = [p[0], p[1]]
                    pasos.append(pp)
        if c1[0] <= c2[0] and c1[1] <= c2[1]:
            p = ["", ""]
            i = 0
            while p[0] != c2[0] and p[1] != c2[1]:
                p[0] = c1[0] + i
                p[1] = c1[1] + i
                pp = [p[0], p[1]]
                pasos.append(pp)
                i += 1
            if p[0] < c2[0]:
                while p[0] < c2[0]:
                    p[0] = p[0] + 1
                    pp = [p[0], p[1]]
                    pasos.append(pp)
        if c1[0] <= c2[0] and c1[1] >= c2[1]:
            p = ["", ""]
            i = 0
            while p[0] != c2[0] and p[1] != c2[1]:
                p[0] = c1[0] + i
                p[1] = c1[1] - i
                pp = [p[0], p[1]]
                pasos.append(pp)
                i += 1
            if p[0] < c2[0]:
                while p[0] < c2[0]:
                    p[0] = p[0] + 1
                    pp = [p[0], p[1]]
                    pasos.append(pp)
         return pasos
           

      




    def distancia(self,other):
        d=((self.px-other.py)**2 + (self.py-other.py)**2)**(0.5)
        return d 
if __name__ == "__main__":
  pass
         