class Vehiculo:
    def __init__(self, matricula=None, marca=None, modelo=None, cliente_id=None):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.cliente_id = cliente_id

    def getMatricula(self):
        return self.matricula

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getCliente_id(self):
        return self.cliente_id

    def setCliente_id(self, cliente_id):
        self.cliente_id = cliente_id
