
# Lucas Guerra Cavalcante

# 1º Exercício de laboratório de Construção de Compiladores
# PAL 1o Avaliação Bimestral

def pal01():
    frase = input("Input: ")

    contadorDeCaracteres = 0
    contadorDeEspacos = 0

    for caractere in frase:  
        contadorDeCaracteres += 1  

        if caractere == " ":
            frase = frase.replace(caractere,"")
            contadorDeEspacos += 1
               

    print("Caracteres:", contadorDeCaracteres)
    print("Espaços:", contadorDeEspacos)
    print(frase)

pal01()