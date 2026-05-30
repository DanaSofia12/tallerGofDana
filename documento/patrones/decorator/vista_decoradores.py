"""Patrón Decorator: capas sobre la vista de validación del Documento."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from documento.entidad.documento import Documento

_CAMPOS_SENSIBLES = ("shipper", "consignee", "notify_party")
_registro_auditoria: list[str] = []


def vista_base(documento: Documento) -> dict[str, Any]:
    return documento.vista_validacion()


def _enmascarar_bloque(datos: dict[str, Any]) -> dict[str, Any]:
    copia = dict(datos)
    for campo in _CAMPOS_SENSIBLES:
        if campo in copia and copia[campo]:
            valor = str(copia[campo])
            copia[campo] = valor[:3] + "***" if len(valor) > 3 else "***"
    return copia


def con_enmascaramiento(
    funcion_vista: Callable[[Documento], dict[str, Any]],
) -> Callable[[Documento], dict[str, Any]]:
    def envoltorio(documento: Documento) -> dict[str, Any]:
        resultado = funcion_vista(documento)
        for bloque in ("digitado", "pdf"):
            if bloque in resultado:
                resultado[bloque] = _enmascarar_bloque(resultado[bloque])
        return resultado

    return envoltorio


def con_auditoria(
    funcion_vista: Callable[[Documento], dict[str, Any]],
) -> Callable[[Documento], dict[str, Any]]:
    def envoltorio(documento: Documento) -> dict[str, Any]:
        _registro_auditoria.append(
            f"Consulta {documento.id_documento} estado={documento.estado}"
        )
        return funcion_vista(documento)

    return envoltorio


def vista_ejecutivo(documento: Documento) -> dict[str, Any]:
    """Vista final: base + enmascaramiento + auditoría."""
    cadena = con_auditoria(con_enmascaramiento(vista_base))
    return cadena(documento)


def obtener_auditoria() -> list[str]:
    return list(_registro_auditoria)
