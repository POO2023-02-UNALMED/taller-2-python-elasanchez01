class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if (tipo == "electrico") or (tipo == "gasolina"):
            self.tipo = tipo

class Asiento: 
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro 
    
    def cambiarColor(self, color):
        if color in ["amarillo", "negro", "verde", "rojo", "blanco"]:
            self.color = color

class Auto():
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self, asientos):
        numAsientos = 0
        for i in range(len(asientos)):
            i+= 1
            numAsientos += 1

            if i >= len(asientos):
                return numAsientos
            
    def verificarIntegridad(self, registro):
        if registro == motor.registro:
            
            for i in range(len(asientos)):
                if (asientos[i] != null and asientos[i].registro != registro):
                    return "Las piezas no son originales"   
                else:
                    return "Auto original"
        else:
            return "Las piezas no son originales"    

    
