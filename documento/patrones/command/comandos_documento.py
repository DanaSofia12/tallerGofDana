"""Patrón Command: acciones encapsuladas como funciones sobre Documento."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from documento.entidad.documento import Documento
from documento.patrones.singleton import servicio_notificacion as notificaciones
from documento.patrones.strategy.comparacion_estrategias import ejecutar_comparacion

HistorialComandos = list[Callable[[], dict[str, Any]]]
_historial: HistorialComandos = []


def aprobar(documento: Documento) -> dict[str, Any]:
    errores = ejecutar_comparacion(documento)
    if errores:
        documento.marcar_errores(errores)
        return {"ok": False, "errores": errores}
    documento.aprobar_ejecutivo()
    return {"ok": True, "estado": documento.estado}


def rechazar(documento: Documento, motivo: str) -> dict[str, Any]:
    documento.marcar_errores([motivo])
    return {"ok": False, "errores": documento.errores_validacion}


def notificar_cliente(documento: Documento, correo: str) -> dict[str, Any]:
    if documento.estado not in (
        "aprobado_ejecutivo",
        "preaviso_enviado",
        "borrador_enviado_cliente",
    ):
        return {"ok": False, "error": "Documento no aprobado por ejecutivo"}
    notificaciones.notificar_cliente_aprobacion(documento, correo)
    return {"ok": True, "estado": documento.estado}


def actualizar_novedad(
    documento: Documento,
    cambios: dict[str, Any],
    correo_cliente: str,
) -> dict[str, Any]:
    documento.registrar_novedad(cambios)
    notificaciones.notificar_novedad(
        documento, correo_cliente, f"Actualización: {cambios}"
    )
    return {"ok": True, "estado": documento.estado}


def ejecutar(comando: Callable[[], dict[str, Any]]) -> dict[str, Any]:
    resultado = comando()
    _historial.append(comando)
    return resultado


def ejecutar_aprobar(documento: Documento) -> dict[str, Any]:
    return ejecutar(lambda: aprobar(documento))


def ejecutar_rechazar(documento: Documento, motivo: str) -> dict[str, Any]:
    return ejecutar(lambda: rechazar(documento, motivo))


def ejecutar_notificar(documento: Documento, correo: str) -> dict[str, Any]:
    return ejecutar(lambda: notificar_cliente(documento, correo))


def cantidad_ejecutados() -> int:
    return len(_historial)
