"""Pruebas del patrón Command."""

import unittest

from documento.entidad.constantes import ESTADO_APROBADO_EJECUTIVO, ESTADO_CON_ERRORES
from documento.patrones.command import comandos_documento as comandos
from documento.patrones.singleton import servicio_notificacion as notificaciones
from tests.helpers import cargar_documento_completo, CARPETA_MAERSK


class TestCommand(unittest.TestCase):
    def setUp(self) -> None:
        notificaciones.reiniciar_para_pruebas()
        comandos._historial.clear()

    def test_ejecutar_aprobar_documento_valido(self) -> None:
        documento = cargar_documento_completo(CARPETA_MAERSK)
        resultado = comandos.ejecutar_aprobar(documento)
        self.assertTrue(resultado["ok"])
        self.assertEqual(documento.estado, ESTADO_APROBADO_EJECUTIVO)

    def test_ejecutar_rechazar_marca_errores(self) -> None:
        documento = cargar_documento_completo(CARPETA_MAERSK)
        resultado = comandos.ejecutar_rechazar(documento, "BL incorrecto")
        self.assertFalse(resultado["ok"])
        self.assertEqual(documento.estado, ESTADO_CON_ERRORES)


if __name__ == "__main__":
    unittest.main()
