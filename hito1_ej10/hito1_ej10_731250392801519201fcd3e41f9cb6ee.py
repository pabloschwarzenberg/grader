u=int(input("usuario:"))
c=int(input("clave:"))
m=int(input("monto:"))
class cajero:
   def __init__(self,us,cl):
       self.us=us
       self.cl=cl
       self.saldo=1000000
       self.saldousuario=100000
   def aprobar(self,u,c):
       b= False
       c=0
       while c<=2:
           
            if self.us!=u and self.cl!=c:
                print("clave invalida")
                c+=1
            if c==3:
               print("tarjeta bloqueada")
               return
              
            if self.us==u and self.cl==c:
               b=True
             
       if b==True:
          if self.saldousuario <= m and self.saldo<=m:
             self.saldousuario=self.saldousuario-m
             self.saldo=self.saldo-m      
             print("saldo cuenta=",self.saldousuario)
             print("saldo cajero=",self.saldo)    
              
#m=int(input())
c1=cajero(10334151,1803)
print(c1.aprobar(u,c))         
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              