"""Patrón Singleton: canal único de notificaciones del proceso."""

from __future__ import annotations

from datetime import datetime
from threading import Lock
from typing import Any

from documento.entidad.documento import Documento

_lock = Lock()
_historial: list[dict[str, Any]] | None = None


def _obtener_historial() -> list[dict[str, Any]]:
    global _historial
    if _historial is None:
        with _lock:
            if _historial is None:
                _historial = []
    return _historial


def enviar(
    destinatario: str,
    asunto: str,
    mensaje: str,
    documento: Documento,
) -> dict[str, Any]:
    registro = {
        "destinatario": destinatario,
        "asunto": asunto,
        "mensaje": mensaje,
        "documento_id": documento.id_documento,
        "fecha": datetime.now().isoformat(timespec="seconds"),
    }
    _obtener_historial().append(registro)
    return registro


def notificar_preaviso(documento: Documento, correo: str) -> None:
    documento.marcar_preaviso()
    enviar(
        correo,
        f"Preaviso documento {documento.numero_bl}",
        "Se validó la información. Revise el borrador adjunto.",
        documento,
    )


def notificar_cliente_aprobacion(documento: Documento, correo: str) -> None:
    documento.notificar_cliente()
    enviar(
        correo,
        f"Documento aprobado {documento.numero_bl}",
        "Su embarque fue validado y aprobado por la empresa.",
        documento,
    )


def notificar_novedad(documento: Documento, correo: str, detalle: str) -> None:
    enviar(
        correo,
        f"Novedad en embarque {documento.numero_bl}",
        detalle,
        documento,
    )


def obtener_historial() -> list[dict[str, Any]]:
    return list(_obtener_historial())


def reiniciar_para_pruebas() -> None:
    global _historial
    with _lock:
        _historial = None
