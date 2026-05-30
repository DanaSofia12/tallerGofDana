"""Registro de datos digitados y extraídos del PDF."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from documento.entidad.constantes import (
    ESTADO_DIGITADO,
    ESTADO_PDF_RECIBIDO,
    ESTADO_RECIBIDO,
)

if TYPE_CHECKING:
    from documento.entidad.documento import Documento


def registrar_digitados(documento: Documento, datos: dict[str, Any]) -> None:
    documento.datos_digitados = dict(datos)
    documento.estado = ESTADO_DIGITADO


def registrar_pdf(documento: Documento, datos: dict[str, Any]) -> None:
    documento.datos_pdf = dict(datos)
    if documento.estado == ESTADO_RECIBIDO:
        documento.estado = ESTADO_PDF_RECIBIDO
