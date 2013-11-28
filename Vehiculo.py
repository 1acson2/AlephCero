class Vehiculo:
    vticket = 0
    
    def __init__(self,longitud,placa,modelo,anyo,color):
        self.__data             = {}
        self.__data['longitud'] = longitud
        self.__data['placa'   ] = placa
        self.__data['modelo'  ] = modelo
        self.__data['anyo'    ] = anyo
        self.__data['color'   ] = color
        self.__data['vticket' ] = Vehiculo.vticket
        Vehiculo.vticket += 1

    def get(self,arg):
        return self.__data.get(arg,'error')

    def set(self,arg,valor):
        if self.get(arg) != 'error':
            self.__data[arg] = valor