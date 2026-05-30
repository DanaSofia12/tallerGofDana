"""Pruebas del patrón Builder."""

import unittest

from documento.patrones.builder import documento_builder as builder
from tests.helpers import CARPETA_MAERSK


class TestBuilder(unittest.TestCase):
    def test_construir_desde_carpeta_maersk(self) -> None:
        estado = builder.desde_carpeta(builder.iniciar(), CARPETA_MAERSK)
        documento = builder.construir(estado)
        self.assertEqual(documento.id_documento, "DOC-2026-001")
        self.assertEqual(documento.numero_bl, "MAEU123456789")
        self.assertTrue(documento.ruta_pdf.endswith(".pdf"))


if __name__ == "__main__":
    unittest.main()
