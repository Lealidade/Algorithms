#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------------------------------------------------------------
class Dicio:
    #-----------------------------------------------
    def __init__(self, chaves=[], valores=[]):
        ''' (Dicio) -> None
        Chamado pelo construtor. 
        RECEBE uma referência self para um objeto Dicio.
        VINCULA os atributos chaves e valores.
        MÉTODO ESPECIAL: usado pelo Python quando escrevemos "objeto_Dicio = Dicio()".
        '''
        self.chaves  = chaves[:]
        self.valores = valores[:]
        
    #---------------------------------------------
    def __str__(self):
        '''(Dicio) -> str 
        RECEBE uma referência self para um objeto Dicio.
        RETORNA uma string que representa o dicionário self.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
               escrevemos "print(objeto_Dicio)" ou "str(objeto Dicio)"
        '''
        s = ''
        # aoelidos
        n = len(self) # usa o método __len__()
        chaves  = self.chaves
        valores = self.valores
        # percorra o dicionário
        for i in range(n):
            s += f"{chaves[i]}: {valores[i]}\n"
        return s    

    #---------------------------------------------    
    def __len__(self):
        '''(Dicio) -> int 
        RECEBE um objeto self da classe Dicio.
        Retorna o número de chaves e self.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos "len(objeto_Dicio)".
        '''
        return len(self.chaves)
    
    #---------------------------------------------        
    def indice(self, chave):
        '''(Dicio, obj) -> int ou None
        RECEBE um objeto self da classe Dicio e um objeto chave.
        RETORNA a posição de chave na lista self.chaves. 
            Se a chave não está no dicionário, o método retorna None.
        '''
        # print("Vixe! Ainda não fiz o método indice() :-(")
        
        for i in range(len(self.chaves)):
            if self.chaves[i] == chave: return i
            
        return None
    
    #---------------------------------------------        
    def put(self, chave, valor):
        '''(Dicio, obj, obje) -> None
        RECEBE um objeto self da classe Dicio e um par de objetos chave-valor.
        INSERE o par chave-valor no dicionário. 
            Se a chave já estiver no dicionário, apenas valor é atualizado.
        '''
        # print("Vixe! Ainda não fiz o método put() :-(")
        
        indiceValue = self.indice(chave)
        
        if indiceValue != None:
            self.chaves[indiceValue] = chave
            self.valores[indiceValue] = valor
        
        self.chaves.append(chave)
        self.valores.append(valor)
        
        return None

    #---------------------------------------------        
    def __setitem__(self, chave, valor):
        '''(Dicio, obj, obje) -> None
        RECEBE um objeto self da classe Dicio e um par de objetos chave-valor.
        INSERE o par chave-valor no dicionário. 
            Se a chave já estiver no dicionário, apenas valor é atualizado.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos "objeto_Dicio[chave] = valor".
        '''
        # print("Vixe! Ainda não fiz o método __setitem__() :-(")
        
        self.put(chave, valor)
        return None

    #---------------------------------------------        
    def get(self, chave):
        '''(Dicio, obj) -> int ou None
        RECEBE um objeto self da classe Dicio e um objeto chave.
        RETORNA o valor em self correspondente à chave. 
            Se have não está no dicionário, o método retorna None.
        '''
        # print("Vixe! Ainda não fiz o método get() :-(")
        
        indice = self.indice(chave)
        
        if indice != None:
            return self.valores[indice]
        
        return None
    
    #---------------------------------------------        
    def __getitem__(self, chave):
        '''(Dicio, obj) -> obj
        RECEBE um objeto self da classe Dicio e um objeto chave.
        RETORNA o valor do dicionario self associado a chave.
            Se a chave não estiver em self, retorna None.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos algo como "valor = objeto_Dicio[chave]".
        '''
        # print("Vixe! Ainda não fiz o método __getitem__() :-(")
        
        return self.get(chave)

    #---------------------------------------------
    def __contains__(self, chave):
        '''
        RECEBE um objeto self da classe Dicio e um objeto chave.
        RETORNA True se chave está em self.chaves e False em caso contrario.
            Se a chave não estiver em self, retorna None.
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos algo como "if chave in objeto_Dicio[chave]: ..."
        '''
        return chave in self.chaves
    
    #---------------------------------------------        
    def keys(self):
        '''(Dicio) -> list
        RECEBE um objeto self da classe Dicio.
        RETORNA uma cópia da lista com suas chaves.
        ''' 
        return self.chaves[:]

    #---------------------------------------------
    def __iter__(self):
        '''
        RECEBE um objeto self da classe Dicio.
        RETORNA um iterador para as chvaes do dicionario
        MÉTODO MÁGICO/ESPECIAL: usado pelo Python quando 
            escrevemos algo como "for chave in objeto_Dicio[chave]: ..."
        '''
        return iter(self.keys())
    
    #---------------------------------------------        
    def values(self):
        '''(Dicio) -> list
        RECEBE um objeto self da classe Dicio.
        RETORNA cópia/clone da lista dos valores em self.
        ''' 
        return self.valores[:]
         
    #---------------------------------------------        
    def items(self):
        '''(Dicio) -> list
        RECEBE um objeto self da classe Dicio.
        RETORNA uma lista com pares da forma (chave, valor) dos itens em self.
        '''
        pares = []
        for i in range(len(self.chaves)):
            chave = self.chaves[i]
            valor = self.valores[i]
            pares.append((chave, valor))
        
        return pares
    

def main():
    ''' 
    Unidade de teste para a classe Dicio
    '''
    print("Testes para a classe Dicio")
    print("--------------------------\n")
    
    # __init__() e __str__()
    print("crie um dicionário vazio")
    d = Dicio()
    print(f"d:\n{d}") 
    pause() # aprecie a paisagem
    
    # put()
    print("\nteste put()")
    d.put('fracassei', 3)
    d.put('em', 1)
    d.put('tudo', 1)
    print(f"d:\n{d}") 
    pause() # aprecie a paisagem
    
    # __setitem__()
    print("\nteste __setitem__()")
    d['o'] = 2
    d['que'] = 3
    d['tentei'] = 4
    print(f"d:\n{d}") 
    pause() # aprecie a paisagem

    # put() e __setitem__()
    print("\nteste put() e __setitem__()")
    d.put('o', 2)
    d['que'] = 1
    d['tentei'] = 5    
    print(f"d:\n{d}") 
    pause() # aprecie a paisagem

    # get()
    print("\nteste get()")
    print(f"d.get('fracassei')={d.get('fracassei')}")
    print(f"d.get('em')={d.get('em')}")
    print(f"d.get('tudo')={d.get('tudo')}\n")
    pause() # aprecie a paisagem

    # __getitem__()
    print("\nteste __getitem__()")
    print(f"d['o']={d['o']}")
    print(f"d['que']={d['que']}")
    print(f"d['tentei']={d['tentei']}")
    print(f"d.get('vida')={d.get('vida')}")
    print(f"d['vida']={d['vida']}\n")
    pause() # aprecie a paisagem

    # mais __setitem__()
    print("\nmais teste __setitem__()")
    d[1] = 'na'
    d[2] = 'vida'
    print(f"d:\n{d}") 
    pause() # aprecie a paisagem

    # teste __contains__()
    print("\nteste __contains__()")
    print(f"'tentei' in d={'tentei' in d}")
    print(f"'1' in d={'1' in d}")
    print(f"1 in d={1 in d}")
    print(f"5 in d={5 in d}\n")
    pause() # aprecie a paisagem
    
    # teste __iter__()
    print("\nteste __iter__()")
    for chave in d: print(f"{chave}: {d[chave]}")
    pause() # aprecie a paisagem

    # teste __len__()
    print("\nteste __len__()")
    print(f"len(d)={len(d)}")
    dicio_vazio = Dicio()
    print(f"len(dicio_vazio)={len(dicio_vazio)}\n")
    pause() # aprecie a paisagem

    # teste keys(), values() e items()
    print("\nteste keys(), values() e items()")
    print(f"d.keys()={d.keys()}")
    print(f"d.values()={d.values()}")
    print(f"d.items()={d.items()}\n")
    pause() # aprecie a paisagem

    print("FIM")

#-----------------------------------------------
def pause():
    input("Tecle ENTER para continuar: ")
    
if __name__ == "__main__":
    main()