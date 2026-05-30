"""Pruebas del patrón Decorator."""

import unittest

from documento.patrones.decorator.vista_decoradores import vista_base, vista_ejecutivo
from tests.helpers import cargar_documento_completo, CARPETA_MAERSK


class TestDecorator(unittest.TestCase):
    def test_vista_ejecutivo_enmascara_shipper(self) -> None:
        documento = cargar_documento_completo(CARPETA_MAERSK)
        base = vista_base(documento)
        ejecutivo = vista_ejecutivo(documento)
        shipper_real = base["digitado"]["shipper"]
        shipper_vista = ejecutivo["digitado"]["shipper"]
        self.assertNotEqual(shipper_real, shipper_vista)
        self.assertTrue(shipper_vista.endswith("***"))


if __name__ == "__main__":
    unittest.main()
