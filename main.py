class Motor:
    def _init_(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    
    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if (tipo == "electrico") or (tipo == "gasolina"):
            self.tipo = tipo

class Asiento: 
    def _init_(self, color, precio, registro)
        self.color = color
        self.precio = precio
        self.registro = registro 
    
    def cambiarColor(self, color):
        if color in ["amarillo", "negro", "amarillo", "rojo", "blanco"]:
            self.color = color

class Auto()