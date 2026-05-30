"""Utilidades compartidas para las pruebas."""

from __future__ import annotations

from pathlib import Path

from documento.entidad.documento import Documento
from documento.patrones.builder import documento_builder as builder
from documento.patrones.factory_method import extraer_desde_documento

RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
CARPETA_MAERSK = RAIZ_PROYECTO / "datos_ejemplo" / "embarque_maersk_directo"
CARPETA_MSC = RAIZ_PROYECTO / "datos_ejemplo" / "embarque_msc_consolidado"


def cargar_documento_completo(carpeta: Path) -> Documento:
    """Carga un Documento con datos PDF y digitados (uso en tests de patrones)."""
    estado = builder.desde_carpeta(builder.iniciar(), carpeta)
    documento = builder.construir(estado)
    documento.registrar_datos_pdf(extraer_desde_documento(documento))
    if documento.datos_digitados:
        documento.registrar_datos_digitados(documento.datos_digitados)
    return documento
