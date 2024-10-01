class Reparacion:
    def __init__(self, reparacion_id=None, hora_entrada=None, hora_salida=None, fecha_entrada=None, fecha_salida=None, matricula=None, cliente_id=None, tipo_servicio=None, pieza_id=None, cantidad_piezas=None):
        self.reparacion_id = reparacion_id
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.matricula = matricula
        self.cliente_id = cliente_id
        self.tipo_servicio = tipo_servicio
        self.pieza_id = pieza_id
        self.cantidad_piezas = cantidad_piezas

    def getReparacion_id(self):
        return self.reparacion_id

    def setReparacion_id(self, reparacion_id):
        self.reparacion_id = reparacion_id

    def getHora_entrada(self):
        return self.hora_entrada

    def setHora_entrada(self, hora_entrada):
        self.hora_entrada = hora_entrada

    def getHora_salida(self):
        return self.hora_salida

    def setHora_salida(self, hora_salida):
        self.hora_salida = hora_salida

    def getFecha_entrada(self):
        return self.fecha_entrada

    def setFecha_entrada(self, fecha_entrada):
        self.fecha_entrada = fecha_entrada

    def getFecha_salida(self):
        return self.fecha_salida

    def setFecha_salida(self, fecha_salida):
        self.fecha_salida = fecha_salida

    def getMatricula(self):
        return self.matricula

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getUsuario_id(self):
        return self.usuario_id

    def setUsuario_id(self, usuario_id):
        self.usuario_id = usuario_id

    def getTipo_servicio(self):
        return self.tipo_servicio

    def setTipo_servicio(self, tipo_servicio):
        self.tipo_servicio = tipo_servicio

    def getPieza_id(self):
        return self.pieza_id

    def setPieza_id(self, pieza_id):
        self.pieza_id = pieza_id

    def getCantidad_piezas(self):
        return self.cantidad_piezas

    def setCantidad_piezas(self, cantidad_piezas):
        self.cantidad_piezas = cantidad_piezas


    def setCliente_id(self, cliente_id):
        self.cliente_id = cliente_id

    def getCliente_id(self):
        return self.cliente_id