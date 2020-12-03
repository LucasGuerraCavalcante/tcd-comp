
# Lucas Guerra Cavalcante - RA: 21804353
# Vijay Lopes Kapoor - RA: 21507579

# Avalição Final : Programas 2 e 3 - devem realizar as seguintes verificações:
# Inicializar a tabela de símbolos com mais de uma palavra-chave;
# Reconhecer números decimais;
# Reconhecer os quatro operadores aritméticos;
# Reconhecer operadores relacionais;
# Reconhecer identificadores e armazená-los na tabela de símbolos;
# Remover espaços em branco, antes e depois de qualquer lexema;
# Remover os dois tipos de comentários da linguagem “C”;
# Tratar erros, gravando mensagem de erro e número da linha onde ocorreu; e

# Recuperar erro de uma posição. Quando encontrar um erro tratá-lo conforme item acima. Ignore esse carac-
# tere não válido, para começar a análise do próximo token a partir do caractere seguinte ao erro.

# -----------------------------------------------------------------------------------------------------------

# Funções:

# Função que analisa e verifica os paratentes 
# Retorna falso se tiver algum parentese errado
def analisarParenteses(texto):
    ct = 0
    for caracter in texto:
        if caracter == '(':
            ct += 1
        if caracter == ')':
            if ct > 0:
                ct -= 1
            else:
                return False

    return ct == 0

# Função que gera a tabela de simbolos
# Retorna a tabela de simbolos de todo o codigo
def gerarTabelaDeSimbolos(texto):
    # Iniciando a tabela de simbolos
    contadorIndetificadores = 0
    tabelaDeSimbolos = []

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

            elif caracter == '!':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Relacional',
                    'id': 'op',
                    'caracter':caracter
                })

            elif caracter == '<':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Relacional',
                    'id': 'op',
                    'caracter':caracter
                })

            elif caracter == '>':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Relacional',
                    'id': 'op',
                    'caracter':caracter
                })

            elif caracter == '&':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Lógico AND',
                    'id': 'op',
                    'caracter':caracter
                })

            elif caracter == '|':
                tabelaDeSimbolos.append({
                    'tipo':'Operador Lógico OR',
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

# Funcao que analisa e remove os comentarios
# Primeiro verifica se nao ha erros com os comentarios
# Posteriormente, se nao haver erros... 
# ...retorna o codigo sem comentarios
def removerECorrigirComentarios(texto):

    errorsInitBlock = [ "/8", "?*", "?8", "?/", "/?"]
    errorsFimBlock = [ "8/", "*?", "8?", "* /"]
    errorsInline = [ "/?", "?/", "/ /", "??", "\\", "\\/", "/\ ", "\/", "||"]
    errorsIniteFim = [ "/8", "?*", "?8", "8/", "*?", "8?", "* /"]

    error = False

    # Comentario de bloco
    if (texto.find("/*") != -1):
        # Dentro de um comentario de bloco com o inicio certo

        for errorFimBlock in errorsFimBlock:

            blocoDeComentario = texto[texto.find("/*")+2:len(texto)]

            if (blocoDeComentario.find(errorFimBlock) != -1):

                error = True

                posicaoDoErro = texto.find(errorFimBlock)

                print(f"O comentário em {posicaoDoErro} deve ser */ e não {errorFimBlock}")
                print(" ")
                print(f"Exemplo: {texto[0:posicaoDoErro-1]} */")
                print(" ")

        if error == False:
            # detecta os cometarios de bloco
            if (texto.find("/*") != -1):
                
                iniciodaAreaComentada = texto.find("/*")
                finalAreaComentada = texto.find("*/")

                try:
                    if texto[finalAreaComentada+2] == ' ':
                        pass
                except:
                    texto = texto[:iniciodaAreaComentada] + "" + texto[finalAreaComentada+2:]
                else:
                    if texto[finalAreaComentada+2] == ' ':
                        texto = texto[:iniciodaAreaComentada] + "" + texto[finalAreaComentada+3:]

                # texto.replace(iniciodaAreaComentada, (texto.find("*/", iniciodaAreaComentada) - iniciodaAreaComentada)+2)

                return texto

    elif (texto.find("*/") != -1):
        # Dentro de um comentario de bloco com o final certo

        # Comentario de bloco inicio errado
        for errorInitBlock in errorsInitBlock:

            if (texto.find(errorInitBlock) != -1):

                error = True

                posicaoDoErro = texto.find(errorInitBlock)

                print(f"O comentário em {posicaoDoErro} deve ser /* e não {errorInitBlock}")
                print(" ")
                print(f"Exemplo: /*{texto[posicaoDoErro+2:len(texto)]}")
                print(" ")

    elif (texto.find("//") != -1): 
        
        # Comentario de linha
        for errorInLine in errorsInline:

            if (texto.find(errorInLine) != -1):

                error = True

                posicaoDoErro = texto.find(errorInLine)

                print(f"O comentário em {posicaoDoErro} deve ser // e não {errorInLine}")
                print(" ")
                print(f"Exemplo: //{texto[posicaoDoErro+2:len(texto)]}")
                print(" ")

        # Comentario de bloco inicio e fim errados
        for errorIniteFim in errorsIniteFim:

            if (texto.find(errorIniteFim) != -1):

                error = True

                posicaoDoErro = texto.find(errorIniteFim)

                print(f"Caracter inesperado: {errorIniteFim} em {posicaoDoErro}")
                print(" ")
                print("Para comentarios de bloco, utilize /* e */")
                print(" ")

        # detecta os cometarios de linha
        if (texto.find("//") != -1):

            iniciodaAreaComentada = texto.find("//")

            texto = texto[:iniciodaAreaComentada] + "" + texto[len(texto):]

            return texto

    else:
        return texto      

## -----------------------------------------------------------------------------------------------------------------------
## -----------------------------------------------------------------------------------------------------------------------
## -----------------------------------------------------------------------------------------------------------------------
## -----------------------------------------------------------------------------------------------------------------------

# Função principal

# Analisador sintatico das expressoes
# Verifica os erros, caso não tenha nenhum...
# ...retorna a tabela de simbolos.
def analisadorSintaticoDeExpresoes(): 
    print("Digite o código: ")
    texto = input()
    print(" ")

    # Remover e analisar comentario
    texto = removerECorrigirComentarios(texto)

    # Analisar uso dos parenteses
    try:
        if analisarParenteses(texto) == False:
            print("Erro Sintático: Os parênteses na expressão não foram utilizados corretamente")
            return print(texto)
    except:
        return print('Para prosseguir, corriga o erro')

    # Verificar se ha alguma expressao (if, while e for)

    if texto.find('if') != -1:
        # Selecionando o conteudo dentro dos parenteses,
        # para uma analise separada
        expressao = texto
        expressao = expressao.replace('(', '')
        expressao = expressao.replace(')', '')

        # Iniciando a analise do if
        operacao = 'if'
        expressao = expressao.replace('if', '', 1)
        tabelaDeSimbolosExpressao = gerarTabelaDeSimbolos(expressao)
        ct = 0
        tamanhoLista = len(tabelaDeSimbolosExpressao)

        # Verificando erros caracter a caracter
        while (ct < tamanhoLista):

            if ct+1 >= tamanhoLista or ct+2 >= tamanhoLista:
                break

            # Duas variáveis seguidas e separadas por espaço em branco
            if tabelaDeSimbolosExpressao[ct]["id"] == "id" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "id":
                print("Erro Sintático: Foram encontradas duas variáveis seguidas e separadas por espaço em branco")
                return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")

            # Dois operadores seguidos separados por espaço em branco
            elif tabelaDeSimbolosExpressao[ct]["id"] == "op" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "op" and tabelaDeSimbolosExpressao[ct+3]["id"] != "num":
                print("Erro Sintático: Foram encontradas dois operadores seguidos separados por espaço em branco.")
                return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")
                    
            ct += 1

    elif texto.find('while') != -1:
        # Selecionando o conteudo dentro dos parenteses,
        # para uma analise separada
        expressao = texto
        expressao = expressao.replace('(', '')
        expressao = expressao.replace(')', '')

        # Iniciando a analise do while
        operacao = 'while'
        expressao = expressao.replace('while', '', 1)
        tabelaDeSimbolosExpressao = gerarTabelaDeSimbolos(expressao)
        ct = 0
        tamanhoLista = len(tabelaDeSimbolosExpressao)

        # Verificando erros caracter a caracter
        while (ct < tamanhoLista):

            if ct+1 >= tamanhoLista or ct+2 >= tamanhoLista:
                break

            # Duas variáveis seguidas e separadas por espaço em branco
            if tabelaDeSimbolosExpressao[ct]["id"] == "id" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "id":
                print("Erro Sintático: Foram encontradas duas variáveis seguidas e separadas por espaço em branco")
                return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")

            # Dois operadores seguidos separados por espaço em branco
            elif tabelaDeSimbolosExpressao[ct]["id"] == "op" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "op" and tabelaDeSimbolosExpressao[ct+3]["id"] != "num":
                print("Erro Sintático: Foram encontradas dois operadores seguidos separados por espaço em branco.")
                return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")
                    
            ct += 1

    elif texto.find('for') != -1:
        # Selecionando o conteudo dentro dos parenteses,
        # para uma analise separada

        expressao = texto
        expressao = expressao.replace('(', '')
        expressao = expressao.replace(')', '')

        # Iniciando a analise do for
        operacao = 'for'
        expressao = expressao.replace('for', '', 1)
        listaParametrosFor = expressao.split(";")

        # Os parametros para o loop for estão incorretos
        if len(listaParametrosFor) != 3:
                print("Erro Sintático: Os parametros para o loop for estão incorretos.")
                return print(texto)
        
        # Percorrendo os paramentros For
        for paramentro in listaParametrosFor: 
            tabelaDeSimbolosExpressao = gerarTabelaDeSimbolos(paramentro)
            ct = 0
            tamanhoLista = len(tabelaDeSimbolosExpressao)

            while (ct < tamanhoLista):

                if ct+1 >= tamanhoLista or ct+2 >= tamanhoLista:
                    break

                # Duas variáveis seguidas e separadas por espaço em branco
                if tabelaDeSimbolosExpressao[ct]["id"] == "id" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "id":
                    print("Erro Sintático: Foram encontradas duas variáveis seguidas e separadas por espaço em branco")
                    return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")

                # Dois operadores seguidos separados por espaço em branco
                elif tabelaDeSimbolosExpressao[ct]["id"] == "op" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "op" and tabelaDeSimbolosExpressao[ct+3]["id"] != "num":
                    print("Erro Sintático: Foram encontradas dois operadores seguidos separados por espaço em branco.")
                    return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")
                        
                ct += 1

    else:
        operacao = False
        ct = 0
        tabelaDeSimbolosExpressao = gerarTabelaDeSimbolos(texto)
        tamanhoLista = len(tabelaDeSimbolosExpressao)

        if texto.find('=') == -1:
             return print("Não há nenhuma expressão válida nesse código")

        # Verificando se há erros 
        while (ct < tamanhoLista):

            if ct+1 >= tamanhoLista or ct+2 >= tamanhoLista:
                break

            if ct == 0 and tabelaDeSimbolosExpressao[ct+2]["tipo"] != "Operador de Atribuição":
                print("Erro Sintático: Foram encontrados mais de um operandos e operadores após o enunciado de atribuição.")
                return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']} {tabelaDeSimbolosExpressao[ct+4]['caracter']}")

            elif tabelaDeSimbolosExpressao[ct]["id"] == "id" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "id":
                print("Erro Sintático: Foram encontradas duas variáveis seguidas e separadas por espaço em branco")
                return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")

            elif tabelaDeSimbolosExpressao[ct]["id"] == "op" and tabelaDeSimbolosExpressao[ct+1]["id"] == "esp" and tabelaDeSimbolosExpressao[ct+2]["id"] == "op":
                print("Erro Sintático: Foram encontradas dois operadores seguidos separados por espaço em branco")
                return print(f"=> {tabelaDeSimbolosExpressao[ct]['caracter']} {tabelaDeSimbolosExpressao[ct+2]['caracter']}")

            ct += 1 

    # Printa o codigo sem espacos e sem comentarios

    texto = texto.replace(" ", "") 
    print('')
    print(texto)
    print('')

    # Printa a tabela de simbolos se não houver erros

    # Printa a tabela de simbolos com operacoes (if, while e for)
    if operacao != False:
    
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

    # Retorna a tabela de simbolos sem as operacoes
    else: 
        ct = 0
        while (ct < tamanhoLista):

            if tabelaDeSimbolosExpressao[ct]["id"] == "esp":
                pass

            elif ct == 0:

                print("--------------------------------------------------")
                print("|     Lexema      |     Token (tipos de token)   |")
                print("--------------------------------------------------")
                print(f"|        {tabelaDeSimbolosExpressao[ct]['caracter']}        |    {tabelaDeSimbolosExpressao[ct]['tipo']}        ")
                print("--------------------------------------------------")

            else:

                print(f"|        {tabelaDeSimbolosExpressao[ct]['caracter']}        |    {tabelaDeSimbolosExpressao[ct]['tipo']}        ")
                print("--------------------------------------------------")

            ct += 1


# Rodando a funcao principal
print('')
analisadorSintaticoDeExpresoes()
print('')