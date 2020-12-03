/*
8o Exercício de Laboratório de Construção de Compiladores
 
(2a Avaliação)
 
LUCAS GUERRA CAVALCANTE
21804353
 
*/
 
#include <iostream>

using namespace std; 

int Prioridade(char c, char t){
    int pc,pt;
    
    if(c == '^')
        pc = 4;
    else if(c == '*' || c == '/')
        pc = 2;
    else if(c == '+' || c == '-')
        pc = 1;
    else if(c == '(')
        pc = 4;
    
    if(t == '^')
        pt = 3;
    else if(t == '*' || t == '/')
        pt = 2;
    else if(t == '+' || t == '-')
        pt = 1;
    else if(t == '(')
        pt = 0;
    
    return (pc > pt);
}

void In2Pos(char expr[]){
    Pilha p;
    int i = 0;
    char c,t;
    
    p = CriaPilha();
    Empilha(p, '(');
    
    do {
        c = expr[i];
        i++;

        if (c >= 'a' && c <= 'z') {
            printf("%c", c);
        }
        else if (c == '(') {
            Empilha(p, '(');
        }
        else if (c == ')' || c == '\0') {
            do {
                t = Desempilha(p);
                if(t != '(')
                    printf("%c", t);
                } while (t != '(') ;
            }
            else if(c == '+' || c == '-' || 
                    c == '*' || c == '/' ||
                    c == '^' ){
            while(1){
                t = Desempilha(p);
                if (Prioridade(c,t)) {
                    Empilha(p, t);
                    Empilha(p, c);
                    break;
                }
                else {
                    printf("%c", t);
                }
            }
        }
    }   while(c != '\0');
    printf("\n");
    LiberaPilha(p);
}

int main() {
  char expr[] = "a*b+c*d^e/f-g*h";
  
  In2Pos(expr);
  return 0;
}
