from Nodo import Nodo

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo  = None

    def __repr__(self):
        cosa = "Cola( "
        aux = self.primero
        while aux != None:
            cosa += (str(aux.info) + " ")
            if (aux.sig != None):
                cosa += "-> "
            aux = aux.sig
        cosa += ")"
        return cosa

    def encolar(self,e):
        aux = Nodo(e)
        if self.primero == None:
            self.primero = aux
            self.ultimo  = aux
        else:
            self.ultimo.sig = aux
            self.ultimo     = aux

    def desencolar(self):
        assert (self.primero != None),"¡Cola vacía!"
        if self.primero == self.ultimo:
            self.primero = None
            self.ultimo  = None
        else:
            self.primero = self.primero.sig

    def 