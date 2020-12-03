"""
4o Exercício de Laboratório de Construção de Compiladores
 
(1a Avaliação)
 
LUCAS GUERRA CAVALCANTE
21804353
 
"""

def errosComentarios():

    print("Digite o código: ")
    texto = input()
    print(" ")

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

                texto = texto[:iniciodaAreaComentada] + "" + texto[finalAreaComentada+2:]

                # texto.replace(iniciodaAreaComentada, (texto.find("*/", iniciodaAreaComentada) - iniciodaAreaComentada)+2)

                print(texto)

    else: 

        if (texto.find("*/") != -1):
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

        else: 
            
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

                print(texto)



errosComentarios()

