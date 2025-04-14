class Node:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, matricula, nome):
        self.raiz = self._inserir(self.raiz, matricula, nome)
        
    def _inserir(self, no, matricula, nome):
        if no is None:
            return Node(matricula, nome)
        if matricula < no.matricula:
            no.esquerda = self._inserir(no.esquerda, matricula, nome)
        elif matricula > no.matricula:
            no.direita = self._inserir(no.direita, matricula, nome)
        else:
            print(f"Matrícula {matricula} já existe.")
        return no

    def buscar(self, matricula):
        def _buscar(no, matricula):
            if no is None:
                return None
            if matricula == no.matricula:
                return no
            elif matricula < no.matricula:
                return _buscar(no.esquerda, matricula)
            else:
                return _buscar(no.direita, matricula)
        return _buscar(self.raiz, matricula)
    
    def ordem(self):
        def _ordem(no):
            if no is not None:
                _ordem(no.esquerda)
                print(f"{no.matricula}: {no.nome}")
                _ordem(no.direita)
        _ordem(self.raiz)
