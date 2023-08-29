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
        c=[]
        o=self.celdas[0]
        m=len(o)
        h=[]
        i=0
        j=0
        u=0
        k=0
        while m>0:
            l=len(o)
            h=[]
            while l>0:
                b=0
                f=len(o)
                while f>0:
                    a=self.celdas[i][j]*other.celdas[u][k]
                    j+=1
                    u+=1
                    b+=a
                    f-=1
                print(b)
                h.append(b)
                j=0
                u=0
                k+=1
                l-=1
            print(h)
            c.append(h)
            k=0
            i+=1
            m-=1
        
            
        print(c)
        p=Matriz(c)
        return p

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           