"""
5o Exercício de Laboratório de Construção de Compiladores
 
(1a Avaliação)
 
LUCAS GUERRA CAVALCANTE
21804353
 
"""
import math

def analisadorLexico(): 
    print("Digite o código: ")
    texto = input()
    print(" ")

    print("--------------------------------------------------")
    print("|     Lexema      |     Token (tipos de token)   |")
    print("--------------------------------------------------")

    contadorIndetificadores = 0

    for caracter in texto: 

        try:
            # Testanto se o caracter pode ser um numero

            int(caracter)

        except ValueError:
            # Caso o catacter nao possa ser um numero

            if caracter == " ":
                pass

            elif caracter == ';' or caracter == '(' or caracter == ')' or caracter == '{' or caracter == '}':
                print(f"|        {caracter}        |           Delimitador        |")
                print("--------------------------------------------------")

            elif caracter == '=':
                print(f"|        {caracter}        |     Operador de Atribuição   |")
                print("--------------------------------------------------")

            elif caracter == '+':
                print(f"|        {caracter}        | Operador de Aritimético ADD  |")
                print("--------------------------------------------------")

            elif caracter == '-':
                print(f"|        {caracter}        | Operador de Aritimético SUB  |")
                print("--------------------------------------------------")

            elif caracter == '*':
                print(f"|        {caracter}        | Operador de Aritimético MULT |")
                print("--------------------------------------------------")

            elif caracter == '/':
                print(f"|        {caracter}        |  Operador de Aritimético DIV |")
                print("--------------------------------------------------")

            else:

                contadorIndetificadores += 1

                print(f"|        {caracter}        |        Identificador {contadorIndetificadores}       |") 
                print("--------------------------------------------------")              


        else: 
            # Se o catacter puder ser um numero

            print(f"|        {caracter}        |             Número           |")
            print("--------------------------------------------------")





analisadorLexico()