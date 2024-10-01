class Cliente:
    def __init__(self, cliente_id=None, nombre=None, telefono=None, usuario_id=None):
        self.cliente_id = cliente_id
        self.nombre = nombre
        self.telefono = telefono
        self.usuario_id = usuario_id

    def getCliente_id(self):
        return self.cliente_id

    def setCliente_id(self, cliente_id):
        self.cliente_id = cliente_id

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getTelefono(self):
        return self.telefono

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getUsuario_id(self):
        return self.usuario_id

    def setUsuario_id(self, usuario_id):
        self.usuario_id = usuario_id
