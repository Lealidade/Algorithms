class Dicio:
    #-----------------------------------------------
    def __init__(self, chaves=[], valores=[]):
        self.chaves  = chaves[:]
        self.valores = valores[:]
        
    #---------------------------------------------
    def __str__(self):
        s = ''
        n = len(self)
        chaves  = self.chaves
        valores = self.valores
        for i in range(n):
            s += f"{chaves[i]}: {valores[i]}\n"
        return s    

    #---------------------------------------------        
    def indice(self, chave):
        for i in range(len(self.chaves)):
            if self.chaves[i] == chave:
                return i
        return None
    
    #---------------------------------------------        
    def put(self, chave, valor):
        indiceValue = self.indice(chave)

        if indiceValue is not None:
            # atualiza o valor existente
            self.valores[indiceValue] = valor
        else:
            # adiciona nova chave e valor
            self.chaves.append(chave)
            self.valores.append(valor)

    #---------------------------------------------        
    def __setitem__(self, chave, valor):
        self.put(chave, valor)

    #---------------------------------------------        
    def get(self, chave):
        indice = self.indice(chave)
        if indice is not None:
            return self.valores[indice]
        return None
    
    #---------------------------------------------        
    def __getitem__(self, chave):
        return self.get(chave)

    #---------------------------------------------    
    def __len__(self):
        return len(self.chaves)

    #---------------------------------------------        
    def keys(self):
        return self.chaves[:]

    #---------------------------------------------        
    def values(self):
        return self.valores[:]
    
    #---------------------------------------------        
    def items(self):
        # Versão usando zip (pode trocar pela de for, se quiser)
        return list(zip(self.chaves, self.valores))

    #---------------------------------------------
    def __contains__(self, chave):
        return chave in self.chaves
    
    #---------------------------------------------
    def __iter__(self):
        return iter(self.keys())