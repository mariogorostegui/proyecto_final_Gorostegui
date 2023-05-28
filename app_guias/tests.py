from django.test import TestCase

from django.db import IntegrityError
from app_guias.models import Usuarios


class UsuariosTests(TestCase):
    """En esta clase van todas las pruebas del modelo Curso."""

    def test_creacion_usuarios(self):
        # caso uso esperado
        usuario = Usuarios(nombre="Pepe", apellido="Lopez",area="RRHH")
        usuario.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Usuarios.objects.count(), 1)
        self.assertIsNotNone(Usuarios.id)
        self.assertEqual(Usuarios.nombre, "Pepe") 
        self.assertEqual(Usuarios.area, "RRHH")

    def test_usuario_str(self):
        usuario = Usuarios(nombre="Pepe", apellido="Lopez",area="RRHH")
        usuario.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(usuario.__str__(), "Pepe Lopez - RRHH")
