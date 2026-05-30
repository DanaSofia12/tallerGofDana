"""Patrón Facade: interfaz única del flujo sobre Documento."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from documento.entidad.documento import Documento
from documento.patrones.builder import documento_builder as builder
from documento.patrones.decorator.vista_decoradores import vista_ejecutivo
from documento.patrones.factory_method.extractor_factory import extraer_desde_documento
from documento.patrones.singleton import servicio_notificacion as notificaciones
from documento.patrones.strategy.comparacion_estrategias import ejecutar_comparacion


def cargar_desde_carpeta(ruta_carpeta: str | Path) -> Documento:
    estado = builder.desde_carpeta(builder.iniciar(), ruta_carpeta)
    documento = builder.construir(estado)
    documento.registrar_datos_pdf(extraer_desde_documento(documento))
    if documento.datos_digitados:
        documento.registrar_datos_digitados(documento.datos_digitados)
    return documento


def pantalla_validacion(documento: Documento) -> dict[str, Any]:
    vista = vista_ejecutivo(documento)
    vista["discrepancias"] = ejecutar_comparacion(documento)
    return vista


def validar_y_resolver(
    documento: Documento,
    aprobado: bool,
    correo_cliente: str,
    correo_interno: str,
) -> dict[str, Any]:
    errores = ejecutar_comparacion(documento)
    if not aprobado or errores:
        documento.marcar_errores(errores or ["Rechazado por ejecutivo"])
        return {
            "ok": False,
            "estado": documento.estado,
            "errores": documento.errores_validacion,
        }
    documento.aprobar_ejecutivo()
    notificaciones.notificar_preaviso(documento, correo_interno)
    documento.marcar_borrador_cliente()
    notificaciones.notificar_cliente_aprobacion(documento, correo_cliente)
    return {"ok": True, "estado": documento.estado, "errores": []}


def aplicar_novedad(
    documento: Documento,
    cambios: dict[str, Any],
    correo_cliente: str,
) -> None:
    documento.registrar_novedad(cambios)
    detalle = ", ".join(f"{k}={v}" for k, v in cambios.items())
    notificaciones.notificar_novedad(documento, correo_cliente, detalle)
