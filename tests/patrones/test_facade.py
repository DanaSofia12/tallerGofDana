"""Pruebas del patrón Facade."""

import unittest

from documento.patrones.facade import proceso_documento_facade as proceso
from documento.patrones.singleton import servicio_notificacion as notificaciones
from tests.helpers import CARPETA_MAERSK


class TestFacade(unittest.TestCase):
    def setUp(self) -> None:
        notificaciones.reiniciar_para_pruebas()

    def test_cargar_desde_carpeta(self) -> None:
        documento = proceso.cargar_desde_carpeta(CARPETA_MAERSK)
        self.assertEqual(documento.id_documento, "DOC-2026-001")
        self.assertTrue(documento.datos_pdf)

    def test_pantalla_validacion_sin_discrepancias(self) -> None:
        documento = proceso.cargar_desde_carpeta(CARPETA_MAERSK)
        pantalla = proceso.pantalla_validacion(documento)
        self.assertIn("discrepancias", pantalla)
        self.assertEqual(pantalla["discrepancias"], [])


if __name__ == "__main__":
    unittest.main()
