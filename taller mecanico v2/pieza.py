class Pieza:
    def __init__(self, pieza_id=None, descripcion=None, stock=None):
        self.pieza_id = pieza_id
        self.descripcion = descripcion
        self.stock = stock

    def getPieza_id(self):
        return self.pieza_id

    def setPieza_id(self, pieza_id):
        self.pieza_id = pieza_id

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getStock(self):
        return self.stock

    def setStock(self, stock):
        self.stock = stock
