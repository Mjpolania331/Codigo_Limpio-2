from usuario import Usuario

class GestorNotas:
    def __init__(self):
        self.usuarios = {}

    def crear_cuenta(self, nombre, contrasena):
        if nombre in self.usuarios:
            return False
        self.usuarios[nombre] = Usuario(nombre, contrasena)
        return True

    def iniciar_sesion(self, nombre, contrasena):
        usuario = self.usuarios.get(nombre)
        if usuario and usuario.contrasena == contrasena:
            return usuario
        return None

    def cambiar_contrasena(self, nombre, nueva_contrasena):
        if nombre in self.usuarios:
            self.usuarios[nombre].contrasena = nueva_contrasena
            return True
        return False