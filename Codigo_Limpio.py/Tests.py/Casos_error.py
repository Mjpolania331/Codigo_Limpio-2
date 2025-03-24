import unittest
from src.gestor_notas import GestorNotas
from src.usuario import Usuario
from src.nota import Nota

class TestCasosError(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorNotas()
        self.usuario = self.gestor.crear_cuenta("juan", "1234")
        self.gestor.iniciar_sesion("juan", "1234")

    # CREAR NOTA
    def test_crear_nota_sin_titulo(self):
        nota = self.usuario.crear_nota("", "Contenido", "Trabajo")
        self.assertIsNone(nota, "Se esperaba que la nota fuera None al no proporcionar un título.")

    def test_crear_nota_sin_contenido(self):
        nota = self.usuario.crear_nota("Titulo", "", "Trabajo")
        self.assertIsNone(nota, "Se esperaba que la nota fuera None al no proporcionar contenido.")

    def test_crear_nota_categoria_invalida(self):
        nota = self.usuario.crear_nota("Titulo", "Contenido", "")
        self.assertIsNone(nota, "Se esperaba que la nota fuera None al proporcionar una categoría inválida.")

    # EDITAR NOTA
    def test_editar_nota_no_existente(self):
        resultado = self.usuario.editar_nota("Inexistente", "Nuevo contenido")
        self.assertFalse(resultado, "Se esperaba que la edición de una nota inexistente devolviera False.")

    def test_editar_nota_sin_contenido(self):
        self.usuario.crear_nota("Proyecto", "Avance", "Trabajo")
        resultado = self.usuario.editar_nota("Proyecto", "")
        self.assertFalse(resultado, "Se esperaba que la edición de la nota con contenido vacío devolviera False.")

    def test_editar_nota_titulo_vacio(self):
        resultado = self.usuario.editar_nota("", "Nuevo contenido")
        self.assertFalse(resultado, "Se esperaba que la edición de la nota con título vacío devolviera False.")

    # ELIMINAR NOTA
    def test_eliminar_nota_no_existente(self):
        resultado = self.usuario.eliminar_nota("Inexistente")
        self.assertFalse(resultado, "Se esperaba que la eliminación de una nota inexistente devolviera False.")

    def test_eliminar_nota_sin_titulo(self):
        resultado = self.usuario.eliminar_nota("")
        self.assertFalse(resultado, "Se esperaba que la eliminación de una nota sin título devolviera False.")

    def test_eliminar_nota_ya_eliminada(self):
        self.usuario.crear_nota("Tarea", "Hacer informe", "Trabajo")
        self.usuario.eliminar_nota("Tarea")
        resultado = self.usuario.eliminar_nota("Tarea")  # Intentar eliminarla de nuevo
        self.assertFalse(resultado, "Se esperaba que la eliminación de una nota ya eliminada devolviera False.")

    # INICIAR SESIÓN
    def test_iniciar_sesion_contrasena_incorrecta(self):
        resultado = self.gestor.iniciar_sesion("juan", "incorrecta")
        self.assertIsNone(resultado, "Se esperaba que la sesión no se iniciara con una contraseña incorrecta.")

    def test_iniciar_sesion_usuario_inexistente(self):
        resultado = self.gestor.iniciar_sesion("pedro", "1234")
        self.assertIsNone(resultado, "Se esperaba que la sesión no se iniciara con un usuario inexistente.")

    def test_iniciar_sesion_sin_credenciales(self):
        resultado = self.gestor.iniciar_sesion("", "")
        self.assertIsNone(resultado, "Se esperaba que la sesión no se iniciara sin credenciales.")

    # CREAR CUENTA
    def test_crear_cuenta_usuario_existente(self):
        resultado = self.gestor.crear_cuenta("juan", "abcd")
        self.assertIsNone(resultado, "Se esperaba que la creación de cuenta devolviera None para un usuario existente.")

    def test_crear_cuenta_sin_usuario(self):
        resultado = self.gestor.crear_cuenta("", "abcd")
        self.assertIsNone(resultado, "Se esperaba que la creación de cuenta devolviera None al no proporcionar un nombre de usuario.")

    def test_crear_cuenta_sin_contrasena(self):
        resultado = self.gestor.crear_cuenta("luis", "")
        self.assertIsNone(resultado, "Se esperaba que la creación de cuenta devolviera None al no proporcionar una contraseña.")

    # CAMBIAR CONTRASEÑA
    def test_cambiar_contrasena_usuario_inexistente(self):
        resultado = self.gestor.cambiar_contrasena("pepe", "4321", "nuevo")
        self.assertFalse(resultado, "Se esperaba que cambiar la contraseña de un usuario inexistente devolviera False.")

    def test_cambiar_contrasena_misma_clave(self):
        resultado = self.gestor.cambiar_contrasena("juan", "1234", "1234")
        self.assertFalse(resultado, "Se esperaba que cambiar la contraseña a la misma clave devolviera False.")

    def test_cambiar_contrasena_sin_nueva(self):
        resultado = self.gestor.cambiar_contrasena("juan", "1234", "")
        self.assertFalse(resultado, "Se esperaba que cambiar la contraseña sin proporcionar una nueva devolviera False.")

if __name__ == '__main__':
    unittest.main()

# Guardar archivo
with open("/mnt/data/Casos_normales.py", "w") as f:
    f.write(normal_cases_code)

/mnt/data/Casos_normales.py

