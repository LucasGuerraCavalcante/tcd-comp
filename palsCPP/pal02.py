"""
2o Exercício de Laboratório de Construção de Compiladores
 
(1a Avaliação)
 
LUCAS GUERRA CAVALCANTE
21804353
 
"""
 
def analisador():
   string = input("Input: ")
 
   # Se a string for toda minuscula
   if string.islower():
       return print("Output: " + string.upper())
 
   # Se a string tiver caracteres maiusculos
   else:
       return print("Output: " + string.lower())
 
analisador()
analisador()
analisador()