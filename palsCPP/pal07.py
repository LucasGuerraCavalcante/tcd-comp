"""
7o Exercício de Laboratório de Construção de Compiladores
 
(2a Avaliação)
 
LUCAS GUERRA CAVALCANTE
21804353
"""

def analisarParenteses(expressao):
    ct = 0
    for caracter in expressao:
        if caracter == '(':
            ct += 1
        if caracter == ')':
            if ct > 0:
                ct -= 1
            else:
                return False

    return ct == 0

def gerarTabelaDeSimbolos(codigo):
    contadorIndetificadores = 0
    tabelaDeSimbolos = []

    for caracter in codigo: 
   
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

            elif caracter == '!':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Lógico',
                    'id': 'op',
                    'caracter':caracter
                })

            elif caracter == '<':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Lógico',
                    'id': 'op',
                    'caracter':caracter
                })

            elif caracter == '>':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Lógico',
                    'id': 'op',
                    'caracter':caracter
                })

            elif caracter == '&':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Lógico',
                    'id': 'op',
                    'caracter':caracter
                })

            elif caracter == '|':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Lógico',
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

    return tabelaDeSimbolos


## -----------------------------------------------------------------------------------------------------------------------
## -----------------------------------------------------------------------------------------------------------------------
## -----------------------------------------------------------------------------------------------------------------------
## -----------------------------------------------------------------------------------------------------------------------

def analisadorSintaticoDeExpresoes(): 
    print("Digite o código: ")
    texto = input()
    print(" ")

    if analisarParenteses(texto) == False:
        print("Erro Sintático: Os parênteses na expressão não foram utilizados corretamente")
        return print(texto)

    expressao = texto
    expressao = expressao.replace('(', '')
    expressao = expressao.replace(')', '')

    if texto.find('if') != -1:
        operacao = 'if'
        expressao = expressao.replace('if', '', 1)
        tabelaDeSimbolosExpressao = gerarTabelaDeSimbolos(expressao)
        ct = 0
        tamanhoLista = len(tabelaDeSimbolosExpressao)

        while (ct < tamanhoLista):

            if ct+1 >= tamanhoLista:
                break

            if tabelaDeSimbolosExpressao[ct]["id"] == "id" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "id":
                print("Erro Sintático: Foram encontradas duas variáveis seguidas e separadas por espaço em branco")
                return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")

            elif tabelaDeSimbolosExpressao[ct]["id"] == "op" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "op" and tabelaDeSimbolosExpressao[ct+3]["id"] != "num":
                print("Erro Sintático: Foram encontradas dois operadores seguidos separados por espaço em branco.")
                return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")

            else: 
                pass
                    
            ct += 1

    elif texto.find('while') != -1:
        operacao = 'while'
        expressao = expressao.replace('while', '', 1)
        tabelaDeSimbolosExpressao = gerarTabelaDeSimbolos(expressao)
        ct = 0
        tamanhoLista = len(tabelaDeSimbolosExpressao)

        while (ct < tamanhoLista):

            if ct+1 >= tamanhoLista:
                break

            if tabelaDeSimbolosExpressao[ct]["id"] == "id" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "id":
                print("Erro Sintático: Foram encontradas duas variáveis seguidas e separadas por espaço em branco")
                return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")

            elif tabelaDeSimbolosExpressao[ct]["id"] == "op" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "op" and tabelaDeSimbolosExpressao[ct+3]["id"] != "num":
                print("Erro Sintático: Foram encontradas dois operadores seguidos separados por espaço em branco.")
                return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")

            else: 
                pass
                    
            ct += 1


    elif texto.find('for') != -1:
        operacao = 'for'
        expressao = expressao.replace('for', '', 1)
        listaParametrosFor = expressao.split(";")

        if len(listaParametrosFor) != 3:
                print("Erro Sintático: Os parametros para o loop for estão incorretos.")
                return print(texto)
        
        for paramentro in listaParametrosFor: 
            tabelaDeSimbolosExpressao = gerarTabelaDeSimbolos(paramentro)
            ct = 0
            tamanhoLista = len(tabelaDeSimbolosExpressao)

            while (ct < tamanhoLista):

                if ct+1 >= tamanhoLista:
                    break

                if tabelaDeSimbolosExpressao[ct]["id"] == "id" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "id":
                    print("Erro Sintático: Foram encontradas duas variáveis seguidas e separadas por espaço em branco")
                    return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")

                elif tabelaDeSimbolosExpressao[ct]["id"] == "op" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "op" and tabelaDeSimbolosExpressao[ct+3]["id"] != "num":
                    print("Erro Sintático: Foram encontradas dois operadores seguidos separados por espaço em branco.")
                    return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")

                else: 
                    pass
                        
                ct += 1

    else:
        print("Erro: Não há nenhuma expressão de if, for or while.")
        return print(texto)  
        

    texto = texto.replace(operacao, '',  1)
    tabelaDeSimbolosGeral = gerarTabelaDeSimbolos(texto)

    ctTabelaGeral = 0
    tamanhoLista = len(tabelaDeSimbolosGeral)
    while (ctTabelaGeral < tamanhoLista):

        if ctTabelaGeral == 0:

            print("--------------------------------------------------")
            print("|     Lexema      |     Token (tipos de token)   |")
            print("--------------------------------------------------")
            print(f"|        {operacao}       |    Comando        ")
            print("--------------------------------------------------")

            if tabelaDeSimbolosGeral[ctTabelaGeral]["id"] == "esp":
                pass

            else: 
                print(f"|        {tabelaDeSimbolosGeral[ctTabelaGeral]['caracter']}        |    {tabelaDeSimbolosGeral[ctTabelaGeral]['tipo']}        ")
                print("--------------------------------------------------")

        else:

            if tabelaDeSimbolosGeral[ctTabelaGeral]["id"] == "esp":
                pass

            else: 
                print(f"|        {tabelaDeSimbolosGeral[ctTabelaGeral]['caracter']}        |    {tabelaDeSimbolosGeral[ctTabelaGeral]['tipo']}        ")
                print("--------------------------------------------------")

        ctTabelaGeral += 1


analisadorSintaticoDeExpresoes()
