#Descomponer un número
numero=int(input())
m_=numero//1000
c_=(numero//100)-m_*10
d_=(numero//10)-(m_*100)-(c_*10)
u_=numero%10
print(m_,"M+",c_,"C+",d_,"D+",u_,"U")