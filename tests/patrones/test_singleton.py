"""Pruebas del patrón Singleton."""

import unittest

from documento.entidad.constantes import ESTADO_APROBADO_EJECUTIVO
from documento.entidad.documento import Documento
from documento.patrones.singleton import servicio_notificacion as notificaciones


class TestSingleton(unittest.TestCase):
    def setUp(self) -> None:
        notificaciones.reiniciar_para_pruebas()

    def test_historial_compartido_entre_llamadas(self) -> None:
        documento = Documento(
            "SNG-01", "maersk", estado=ESTADO_APROBADO_EJECUTIVO, numero_bl="BL-SNG"
        )
        notificaciones.notificar_preaviso(documento, "interno@empresa.com")
        notificaciones.notificar_cliente_aprobacion(documento, "cliente@ejemplo.com")
        self.assertEqual(len(notificaciones.obtener_historial()), 2)

    def test_reiniciar_deja_historial_vacio(self) -> None:
        documento = Documento("SNG-02", "msc", estado=ESTADO_APROBADO_EJECUTIVO)
        notificaciones.enviar("a@b.com", "asunto", "mensaje", documento)
        notificaciones.reiniciar_para_pruebas()
        self.assertEqual(notificaciones.obtener_historial(), [])


if __name__ == "__main__":
    unittest.main()
