"""Pruebas del patrón Factory Method."""

import unittest

from documento.patrones.builder import documento_builder as builder
from documento.patrones.factory_method import extraer_desde_documento
from tests.helpers import CARPETA_MAERSK, CARPETA_MSC


class TestFactoryMethod(unittest.TestCase):
    def test_extraer_formato_maersk(self) -> None:
        documento = builder.construir(
            builder.desde_carpeta(builder.iniciar(), CARPETA_MAERSK)
        )
        datos = extraer_desde_documento(documento)
        self.assertEqual(datos["formato"], "maersk")

    def test_extraer_formato_msc(self) -> None:
        documento = builder.construir(
            builder.desde_carpeta(builder.iniciar(), CARPETA_MSC)
        )
        datos = extraer_desde_documento(documento)
        self.assertEqual(datos["formato"], "msc")

    def test_naviera_desconocida_lanza_error(self) -> None:
        documento = builder.construir(builder.iniciar())
        documento.naviera = "naviera_inexistente"
        with self.assertRaises(ValueError):
            extraer_desde_documento(documento)


if __name__ == "__main__":
    unittest.main()
