import unittest
from src.gestor_notas import GestorNotas
from src.usuario import Usuario
from src.nota import Nota

class TestCasosExtremos(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorNotas()
        self.usuario = self.gestor.crear_cuenta("juan", "1234")
        self.gestor.iniciar_sesion("juan", "1234")

    # CREAR NOTA
    def test_crear_nota_contenido_largo(self):
        contenido_largo = "a" * 5000
        nota = self.usuario.crear_nota("Ensayo", contenido_largo, "Academico")
        self.assertEqual(len(nota.contenido), 5000)

    def test_crear_nota_titulo_largo(self):
        titulo_largo = "T" * 100
        nota = self.usuario.crear_nota(titulo_largo, "Contenido", "Academico")
        self.assertEqual(len(nota.titulo), 100)

    def test_crear_nota_categoria_invalida(self):
        nota = self.usuario.crear_nota("Ensayo", "Contenido", "X" * 50)
        self.assertIsNone(nota)

    # EDITAR NOTA
    def test_editar_nota_vacia(self):
        self.usuario.crear_nota("Proyecto", "Avance 1", "Trabajo")
        resultado = self.usuario.editar_nota("Proyecto", "")
        self.assertFalse(resultado)

    def test_editar_nota_contenido_largo(self):
        contenido_largo = "b" * 5000
        self.usuario.crear_nota("Reporte", "Borrador", "Academico")
        resultado = self.usuario.editar_nota("Reporte", contenido_largo)
        self.assertTrue(resultado)

    def test_editar_nota_titulo_largo(self):
        titulo_largo = "X" * 100
        self.usuario.crear_nota(titulo_largo, "Contenido", "Trabajo")
        resultado = self.usuario.editar_nota(titulo_largo, "Nuevo contenido")
        self.assertTrue(resultado)

    # ELIMINAR NOTA
    def test_eliminar_nota_titulo_largo(self):
        titulo_largo = "A" * 100
        self.usuario.crear_nota(titulo_largo, "Contenido", "Trabajo")
        resultado = self.usuario.eliminar_nota(titulo_largo)
        self.assertTrue(resultado)

    def test_eliminar_nota_con_caracteres_especiales(self):
        titulo_especial = "@#€$%&*!"
        self.usuario.crear_nota(titulo_especial, "Contenido", "Personal")
        resultado = self.usuario.eliminar_nota(titulo_especial)
        self.assertTrue(resultado)

    def test_eliminar_nota_con_espacios(self):
        titulo_con_espacios = "    Nota con espacios    "
        self.usuario.crear_nota(titulo_con_espacios, "Contenido", "Trabajo")
        resultado = self.usuario.eliminar_nota(titulo_con_espacios)
        self.assertTrue(resultado)

    # INICIAR SESIÓN
    def test_iniciar_sesion_usuario_largo(self):
        usuario_largo = "x" * 100
        self.gestor.crear_cuenta(usuario_largo, "1234")
        resultado = self.gestor.iniciar_sesion(usuario_largo, "1234")
        self.assertTrue(resultado)

    def test_iniciar_sesion_con_caracteres_especiales(self):
        usuario_especial = "!@#$%^&*()"
        self.gestor.crear_cuenta(usuario_especial, "abcd1234")
        resultado = self.gestor.iniciar_sesion(usuario_especial, "abcd1234")
        self.assertTrue(resultado)

    def test_iniciar_sesion_con_espacios(self):
        usuario_con_espacios = "   usuario   "
        self.gestor.crear_cuenta(usuario_con_espacios, "5678")
        resultado = self.gestor.iniciar_sesion(usuario_con_espacios, "5678")
        self.assertTrue(resultado)

    # CREAR CUENTA
    def test_crear_cuenta_contrasena_corta(self):
        usuario = self.gestor.crear_cuenta("carlos", "12")
        self.assertIsNone(usuario)

    def test_crear_cuenta_nombre_largo(self):
        usuario_largo = "u" * 100
        usuario = self.gestor.crear_cuenta(usuario_largo, "password123")
        self.assertIsNotNone(usuario)

    def test_crear_cuenta_con_caracteres_especiales(self):
        usuario_especial = "#$%&'()*+"
        usuario = self.gestor.crear_cuenta(usuario_especial, "segura123")
        self.assertIsNotNone(usuario)

    # CAMBIAR CONTRASEÑA
    def test_cambiar_contrasena_misma(self):
        resultado = self.gestor.cambiar_contrasena("juan", "1234", "1234")
        self.assertFalse(resultado)

    def test_cambiar_contrasena_muy_larga(self):
        resultado = self.gestor.cambiar_contrasena("juan", "1234", "x" * 100)
        self.assertTrue(resultado)

    def test_cambiar_contrasena_con_caracteres_especiales(self):
        resultado = self.gestor.cambiar_contrasena("juan", "1234", "@NewPass123!")
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()