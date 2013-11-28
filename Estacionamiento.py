from Cola import Cola
from Tubo import Tubo

class Estacionamiento(Cola):
    def generar(self):
        nuevo = Tubo()
        self.encolar(nuevo)

    def destruir(self):
        self.desencolar()

    def estacionar(self,vehiculo):
        return ticket
    
    def retirar(self,placa,ticket):

    def existe(self,placa,ticket):
        return existe

    def vaciar(self,ticket):
        aux = self.primero
        while ((aux.ticket != ticket) and (aux != None)):
            aux = aux.sig
        if aux = None:
            print('No existe tubo con etiqueta '+ticket+'.')
        else:
            while aux.ocupacion > 0:
                self.estacionar(aux.vehiculos.tope())
                aux.retirar()
