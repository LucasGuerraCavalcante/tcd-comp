/*
3o Exercício de Laboratório de Construção de Compiladores
 
(1a Avaliação)
 
LUCAS GUERRA CAVALCANTE
21804353
 
*/
 
#include <iostream>
#include <fstream>
#include <string>

using namespace std; 

int main() {

    string arquivo;
    ifstream readFile("textcode.txt");

    getline(readFile, arquivo, '\0');

    // detecta os cometarios de bloco
    while(arquivo.find("/*") != string::npos) {

        size_t iniciodaAreaComentada = arquivo.find("/*");

        arquivo.erase(iniciodaAreaComentada, (arquivo.find("*/", iniciodaAreaComentada) - iniciodaAreaComentada)+2);
    }

    // detecta os cometarios de linha
    while(arquivo.find("//") != string::npos) {

        size_t iniciodaAreaComentada = arquivo.find("//");

        arquivo.erase(iniciodaAreaComentada, arquivo.find("\n", iniciodaAreaComentada) - iniciodaAreaComentada);
    }

    cout << arquivo;

    return 0;
}













// size_t -> Tipo de inteiro para resltados do operador sizeof
// string::npos -> Valor máximo para um size_t

