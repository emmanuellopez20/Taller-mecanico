class Usuario:
    def __init__(self, usuario_id=None, nombre="", username="", password="", perfil=""):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.username = username
        self.password = password
        self.perfil = perfil

    def getUsuario_id(self):
        return self.usuario_id

    def setUsuario_id(self, usuario_id):
        self.usuario_id = usuario_id

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def getPerfil(self):
        return self.perfil

    def setPerfil(self, perfil):
        self.perfil = perfil
