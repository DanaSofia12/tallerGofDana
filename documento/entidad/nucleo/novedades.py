"""Actualización por novedades operativas (fechas, barco, etc.)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from documento.entidad.constantes import ESTADO_NOVEDAD

if TYPE_CHECKING:
    from documento.entidad.documento import Documento


def aplicar_cambios(documento: Documento, cambios: dict[str, Any]) -> None:
    for clave, valor in cambios.items():
        if clave in documento.datos_digitados:
            documento.datos_digitados[clave] = valor
        if clave in documento.datos_pdf:
            documento.datos_pdf[clave] = valor
        if hasattr(documento, clave):
            setattr(documento, clave, valor)
    documento.estado = ESTADO_NOVEDAD
