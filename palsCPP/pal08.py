"""
8o Exercício de Laboratório de Construção de Compiladores
 
(2a Avaliação)
 
LUCAS GUERRA CAVALCANTE
21804353
 
"""

# Classe Pilha 

class Pilha: 

    def __init__(self):
        self.items = []

    def esta_vazia(self):
        if self.items == []:
            return True 
        else:
            return False
      
    def tamanho(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.esta_vazia() == True:
            return print("A pilha está vazia")
        else:
            return self.items.pop()

    def peek(self):
        if self.esta_vazia() == True:
            return print("A pilha está vazia")
        else:
           return self.items[-1]     

    def mostrar(self):
        print(self.items)

# Funções 

def prioridadeOperador(operador):
    if operador == '+' or operador == '-':
        return 1
    elif operador == '*' or operador == '/' or operador == '%':
        return 2
    elif operador == '^':
        return 3  
    else:
        return 0

def converter(operacao):
    resultado = ""
    pilha = Pilha()

    for caracter in operacao: 
        if caracter == ' ' or caracter == '\t':
            pass
        elif caracter in '+-*/&^':
            while not pilha.esta_vazia() and prioridadeOperador(pilha.peek()) >= prioridadeOperador(caracter):
                resultado = resultado + pilha.pop()
            pilha.push(caracter)
        else: 
            resultado = resultado + caracter

    while not pilha.esta_vazia():
        resultado = resultado + pilha.pop()

    return resultado

# Main

print("Expressão infixa: ")
expressao = input()

print(converter(expressao))

