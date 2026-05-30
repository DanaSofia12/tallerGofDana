"""Consultas y vista de datos del Documento."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from documento.entidad.constantes import CAMPOS_COMPARABLES

if TYPE_CHECKING:
    from documento.entidad.documento import Documento


def campos_comparables(documento: Documento) -> list[str]:
    return list(CAMPOS_COMPARABLES)


def vista_para_validacion(documento: Documento) -> dict[str, Any]:
    return {
        "id": documento.id_documento,
        "estado": documento.estado,
        "digitado": dict(documento.datos_digitados),
        "pdf": dict(documento.datos_pdf),
        "errores": list(documento.errores_validacion),
    }
