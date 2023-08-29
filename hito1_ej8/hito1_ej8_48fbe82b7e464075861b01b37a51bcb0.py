n=eval(input())
MI=n//1000
CE=(n-(MI*1000))//100
DE=(n-(MI*1000)-(CE*100))//10
UN=(n-(MI*1000)-(CE*100)-(DE*10))//1

MI=str(MI)
CE=str(CE)
DE=str(DE)
UN=str(UN)

M=str("M")
C=str("C")
D=str("D")
U=str("U")

plus=str("+")

print(MI+M+plus+CE+C+plus+DE+D+plus+UN+U)
