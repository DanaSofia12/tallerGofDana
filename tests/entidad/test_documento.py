"""Pruebas de la entidad Documento."""

import unittest

from documento.entidad.constantes import ESTADO_DIGITADO, ESTADO_EN_VALIDACION
from documento.entidad.documento import Documento


class TestDocumento(unittest.TestCase):
    def test_registrar_datos_digitados_cambia_estado(self) -> None:
        documento = Documento("T-001", "maersk")
        documento.registrar_datos_digitados({"numero_bl": "BL-100"})
        self.assertEqual(documento.estado, ESTADO_DIGITADO)
        self.assertEqual(documento.datos_digitados["numero_bl"], "BL-100")

    def test_marcar_en_validacion(self) -> None:
        documento = Documento("T-002", "msc", estado=ESTADO_DIGITADO)
        documento.marcar_en_validacion()
        self.assertEqual(documento.estado, ESTADO_EN_VALIDACION)

    def test_vista_validacion_contiene_bloques(self) -> None:
        documento = Documento("T-003", "cosco")
        documento.registrar_datos_pdf({"numero_bl": "PDF-1"})
        vista = documento.vista_validacion()
        self.assertIn("digitado", vista)
        self.assertIn("pdf", vista)
        self.assertEqual(vista["pdf"]["numero_bl"], "PDF-1")


if __name__ == "__main__":
    unittest.main()
