import unittest
from src.gestor_notas import GestorNotas
from src.usuario import Usuario
from src.nota import Nota

class TestCasosNormales(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorNotas()
        self.usuario = self.gestor.crear_cuenta("juan", "1234")
        self.gestor.iniciar_sesion("juan", "1234")

    # CREAR CUENTA
    def test_crear_cuenta(self):
        usuario = self.gestor.crear_cuenta("ana", "5678")
        self.assertIsNotNone(usuario)

    def test_crear_cuenta_con_nuevo_usuario(self):
        usuario = self.gestor.crear_cuenta("carlos", "abcd")
        self.assertIsNotNone(usuario)

    def test_crear_cuenta_con_usuario_y_contrasena_normales(self):
        usuario = self.gestor.crear_cuenta("maria", "contraseñaSegura")
        self.assertIsNotNone(usuario)

    # INICIAR SESIÓN
    def test_iniciar_sesion(self):
        resultado = self.gestor.iniciar_sesion("juan", "1234")
        self.assertTrue(resultado)

    def test_iniciar_sesion_con_otro_usuario(self):
        self.gestor.crear_cuenta("ana", "5678")
        resultado = self.gestor.iniciar_sesion("ana", "5678")
        self.assertTrue(resultado)

    def test_iniciar_sesion_despues_de_cerrar_sesion(self):
        self.gestor.cerrar_sesion()
        resultado = self.gestor.iniciar_sesion("juan", "1234")
        self.assertTrue(resultado)

    # CREAR NOTA
    def test_crear_nota(self):
        nota = self.usuario.crear_nota("Tarea", "Hacer informe", "Trabajo")
        self.assertEqual(nota.titulo, "Tarea")

    def test_crear_nota_con_diferente_categoria(self):
        nota = self.usuario.crear_nota("Lista de compras", "Comprar leche y pan", "Personal")
        self.assertEqual(nota.categoria, "Personal")

    def test_crear_nota_con_diferente_contenido(self):
        nota = self.usuario.crear_nota("Proyecto", "Avance inicial", "Trabajo")
        self.assertEqual(nota.contenido, "Avance inicial")

    # EDITAR NOTA
    def test_editar_nota(self):
        self.usuario.crear_nota("Tarea", "Hacer informe", "Trabajo")
        resultado = self.usuario.editar_nota("Tarea", "Entregar mañana")
        self.assertTrue(resultado)

    def test_editar_nota_cambiar_titulo(self):
        self.usuario.crear_nota("Examen", "Estudiar álgebra", "Academico")
        resultado = self.usuario.editar_nota("Examen", "Estudiar cálculo")
        self.assertTrue(resultado)

    def test_editar_nota_cambiar_categoria(self):
        self.usuario.crear_nota("Agenda", "Reunión a las 10AM", "Trabajo")
        resultado = self.usuario.editar_nota("Agenda", "Reunión a las 10AM y almuerzo", "Personal")
        self.assertTrue(resultado)

    # ELIMINAR NOTA
    def test_eliminar_nota(self):
        self.usuario.crear_nota("Tarea", "Hacer informe", "Trabajo")
        resultado = self.usuario.eliminar_nota("Tarea")
        self.assertTrue(resultado)

    def test_eliminar_nota_recien_creada(self):
        self.usuario.crear_nota("Nuevo proyecto", "Definir objetivos", "Trabajo")
        resultado = self.usuario.eliminar_nota("Nuevo proyecto")
        self.assertTrue(resultado)

    def test_eliminar_nota_despues_de_editarla(self):
        self.usuario.crear_nota("Evento", "Concierto el sábado", "Ocio")
        self.usuario.editar_nota("Evento", "Concierto el domingo")
        resultado = self.usuario.eliminar_nota("Evento")
        self.assertTrue(resultado)

    # CAMBIAR CONTRASEÑA
    def test_cambiar_contrasena(self):
        resultado = self.gestor.cambiar_contrasena("juan", "1234", "nueva123")
        self.assertTrue(resultado)

    def test_cambiar_contrasena_y_volver_a_iniciar_sesion(self):
        self.gestor.cambiar_contrasena("juan", "1234", "nueva123")
        resultado = self.gestor.iniciar_sesion("juan", "nueva123")
        self.assertTrue(resultado)

    def test_cambiar_contrasena_varias_veces(self):
        self.gestor.cambiar_contrasena("juan", "1234", "clave1")
        self.gestor.cambiar_contrasena("juan", "clave1", "clave2")
        resultado = self.gestor.iniciar_sesion("juan", "clave2")
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()