''' 
Escreva uma função que recebe uma lista com números e, usando o comando for,
procura e retorna o valor mínimo desses números e o índice onde esse valor ocorre.
Por exemplo, para a lista [5, 0, 7, -3, 9], o menor valor é -3 que ocorre no 
índice 3.
'''

def main():
    print("Iniciando o programa com 3 testes")
    print("\nLista: [5,0,7,-3,9]\n", menor([5,0,7,-3,9]))
    print("\nLista: [13,8,5,78,19]\n", menor([13,8,5,78,19]))
    print("\nLista: [-13,-8,-5,-78,-19]\n", menor([-13,-8,-5,-78,-19]))

#------------------------------------------   
def menor(lista):
    ''' (list) -> list
      Recebe uma lista e retorna uma dicionário contendo o menor
      valor da lista e indice que contem esse menor numero.
    '''
    
    n = len(lista) # tamanho da lista
    
    # Inicialização
    menorNumero = lista[0]
    indiceDoMenorNumero = 0
    
    
    for i in range(n-1):
        if(lista[i+1] < menorNumero):
            menorNumero = lista[i+1]
            indiceDoMenorNumero = i+1
    
    resultado = {
        "menor número": menorNumero,
        "índice do menor número": indiceDoMenorNumero
    }
    
    return resultado

#------------------------------------------    
# inicio do programa: chamada da funcao main()    
if __name__ == "__main__":
    main()
    