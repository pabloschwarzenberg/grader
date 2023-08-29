def validar_expresion(expresion):
      que=len(expresion)
      def Valido(n):
        if n==1 and (expresion[n-1] in ['0','1','2','3','4','5','6','7','8','9'] or (expresion[n-1] in ['+','-'] and expresion[n] in ['0','1','2','3','4','5','6','7','8','9']) or (expresion[n] in ['+','-'] and expresion[n-1] in ['0','1','2','3','4','5','6','7','8','9'])):
            return True
        elif n==len(expresion) and expresion[n-1] not in ['0','1','2','3','4','5','6','7','8','9']:
          return False
        elif (expresion[n-1] in ['+','-'] and expresion[n-2] in ['0','1','2','3','4','5','6','7','8','9']) or (expresion[n-1] in ['0','1','2','3','4','5','6','7','8','9'] and expresion[n-2] not in ['0','1','2','3','4','5','6','7','8','9']) or (expresion[n-1] in ['0','1','2','3','4','5','6','7','8','9'] and expresion[n-2] in ['0','1','2','3','4','5','6','7','8','9']):
          return Valido(n-1)
        else:
          return False
      return Valido(que)          