"""
6o Exercício de Laboratório de Construção de Compiladores
 
(2a Avaliação)
 
LUCAS GUERRA CAVALCANTE
21804353
 
"""
import math

def analisadorLexicoESintatico(): 
    print("Digite o código: ")
    texto = input()
    print(" ")

    contadorIndetificadores = 0
    tabelaDeSimbolos = []

    # Construindo a tabela de simbolos 

    for caracter in texto: 
   
        try:
            # Testanto se o caracter pode ser um numero

            int(caracter)

        except ValueError:
            # Caso o caracter nao possa ser um numero

            if caracter == " ":
                tabelaDeSimbolos.append({
                    'tipo':'Espaço em branco',
                    'id': 'esp',
                    'caracter':' '
                })

            elif caracter == ';' or caracter == '(' or caracter == ')' or caracter == '{' or caracter == '}':
                tabelaDeSimbolos.append({
                    'tipo':'Delimitador',
                    'id': 'del',
                    'caracter':caracter
                })

            elif caracter == '=':
                tabelaDeSimbolos.append({
                    'tipo':'Operador de Atribuição',
                    'id': 'op',
                    'caracter':caracter
                })

            elif caracter == '+':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Aritimético ADD',
                    'id': 'op',
                    'caracter':caracter
                })

            elif caracter == '-':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Aritimético SUB',
                    'id': 'op',
                    'caracter':caracter
                })

            elif caracter == '*':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Aritimético MULT',
                    'id': 'op',
                    'caracter':caracter
                })

            elif caracter == '/':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Aritimético DIV',
                    'id': 'op',
                    'caracter':caracter
                })

            else:

                contadorIndetificadores += 1
                tabelaDeSimbolos.append({
                    'tipo': f'Identificador {contadorIndetificadores}',
                    'id': 'id',
                    'caracter':caracter
                })         

        else: 
            # Se o caracter puder ser um numero
            tabelaDeSimbolos.append({
                    'tipo': f'Número {contadorIndetificadores}',
                    'id': 'num',
                    'caracter':caracter
                })

    ct = 0
    tamanhoLista = len(tabelaDeSimbolos)

    # Verificando se há erros 
    while (ct < tamanhoLista):

        if ct+1 >= tamanhoLista:
            break

        if ct == 0 and tabelaDeSimbolos[ct+2]["tipo"] != "Operador de Atribuição":
            print("Erro Sintático: Foram encontrados mais de um operandos e operadores após o enunciado de atribuição.")
            return print(f"=> {tabelaDeSimbolos[ct]['caracter']} {tabelaDeSimbolos[ct+2]['caracter']} {tabelaDeSimbolos[ct+4]['caracter']}")

        elif tabelaDeSimbolos[ct]["id"] == "id" and tabelaDeSimbolos[ct+1]["id"] == "esp" and tabelaDeSimbolos[ct+2]["id"] == "id":
            print("Erro Sintático: Foram encontradas duas variáveis seguidas e separadas por espaço em branco")
            return print(f"=> {tabelaDeSimbolos[ct]['caracter']} {tabelaDeSimbolos[ct+2]['caracter']}")

        elif tabelaDeSimbolos[ct]["id"] == "op" and tabelaDeSimbolos[ct+1]["id"] == "esp" and tabelaDeSimbolos[ct+2]["id"] == "op":
            print("Erro Sintático: Foram encontradas dois operadores seguidos separados por espaço em branco”.")
            return print(f"=> {tabelaDeSimbolos[ct]['caracter']} {tabelaDeSimbolos[ct+2]['caracter']}")

        else: 
            pass

        ct += 1

    ct = 0
    # Retorna a tabela de simbolos se não houver erros
    while (ct < tamanhoLista):

        if tabelaDeSimbolos[ct]["id"] == "esp":
            pass

        elif ct == 0:

            print("--------------------------------------------------")
            print("|     Lexema      |     Token (tipos de token)   |")
            print("--------------------------------------------------")
            print(f"|        {tabelaDeSimbolos[ct]['caracter']}        |    {tabelaDeSimbolos[ct]['tipo']}        ")
            print("--------------------------------------------------")

        else:

            print(f"|        {tabelaDeSimbolos[ct]['caracter']}        |    {tabelaDeSimbolos[ct]['tipo']}        ")
            print("--------------------------------------------------")

        ct += 1



analisadorLexicoESintatico()