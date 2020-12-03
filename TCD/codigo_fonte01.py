
# Lucas Guerra Cavalcante - RA: 21804353
# Vijay Lopes Kapoor - RA: 21507579

# Programa 01 – devera traduzir as expressões infixas com:
# * Números inteiros de um e/ou mais de um dígito;
# * Os operadores aritméticos (* , / , + , - ); e
# * Espaços.

# -----------------------------------------------------------------------------------------------------------

# Classe Pilha:

# Os caracteres serão organizados em uma PILHA
# A classe possui os métodos tradicionais... 
# ...para que se possa trabalhar com uma pilha

class Pilha: 

    def __init__(self):
        self.items = []

    def estaVazia(self):
        if self.items == []:
            return True 
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.estaVazia() == True:
            return print("A pilha está vazia")
        else:
            return self.items.pop()

    def conferirUltimoItem(self):
        if self.estaVazia() == True:
            return print("A pilha está vazia")
        else:
           return self.items[-1]   
           
# Funções:

# Função que analisa e determina o peso (prioridade) do operador
def prioridadeOperador(operador):
    if operador == '+' or operador == '-':
        return 1
    elif operador == '*' or operador == '/' or operador == '%':
        return 2
    elif operador == '^':
        return 3  
    else:
        return 0

# Função que analisa e corrige os espaços no final da conversão
# Faz a correção se e somente se tiver espaços duplicados
def corrigirEspacos(resultado):
    ct = 0
    resultadoCorrigido = ''

    while ct != len(resultado):
        if resultado[ct] == ' ' and resultado[ct+1] == ' ':
            resultadoCorrigido = resultadoCorrigido
        else:
            resultadoCorrigido = resultadoCorrigido + resultado[ct]
        
        ct += 1

    return resultadoCorrigido

# Função realiza a converssão uma operação infixa para posfixa
def converter(operacao):

    resultado = ""

    # Implementando a classe Pilha
    pilha = Pilha()

    # Loop para analisar caracter a caracter
    for caracter in operacao: 

        # Teste dos operadores
        if caracter in '+-*/&^':

            # Verificando os pesos dos operadores
            while not pilha.estaVazia() and prioridadeOperador(pilha.conferirUltimoItem()) >= prioridadeOperador(caracter):
                resultado = resultado + pilha.pop()
    
            pilha.push(caracter)
        else: 
            # Caso for um caracter alfanumerico
            resultado = resultado + caracter

    while not pilha.estaVazia():
        resultado = resultado + pilha.pop()

    # Utilizando a função corrigirEspacos
    resultadoCorrigido = corrigirEspacos(resultado)

    return resultadoCorrigido  

# Função Main

def main():
    print("Expressão infixa: ")
    expressao = input()
    print('')
    print("Expressão posfixa: ")
    print(converter(expressao))

main()


