"""Pruebas del patrón Strategy."""

import unittest

from documento.entidad.constantes import ESTADO_EN_VALIDACION
from documento.patrones.strategy import ejecutar_comparacion
from tests.helpers import cargar_documento_completo, CARPETA_MAERSK, CARPETA_MSC


class TestStrategy(unittest.TestCase):
    def test_maersk_directo_sin_discrepancias(self) -> None:
        documento = cargar_documento_completo(CARPETA_MAERSK)
        errores = ejecutar_comparacion(documento)
        self.assertEqual(errores, [])
        self.assertEqual(documento.estado, ESTADO_EN_VALIDACION)

    def test_msc_consolidado_sin_discrepancias(self) -> None:
        documento = cargar_documento_completo(CARPETA_MSC)
        errores = ejecutar_comparacion(documento)
        self.assertEqual(errores, [])


if __name__ == "__main__":
    unittest.main()
