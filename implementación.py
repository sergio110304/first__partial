class Tablero: 
    def __init__(self, minas:str, numeros:str):
        self.minas = minas
        self.numeros = numeros

    ## Esta vaina no sirve
    
    
class Numeros: 
    def alrededor(self):
        pass

class Minas: 
    def __init__(self, posicion:str):
        self.posicion = posicion
    def explotar(self):
        pass

class Jugador: 
    def seleccionar(self):
        pass
        
