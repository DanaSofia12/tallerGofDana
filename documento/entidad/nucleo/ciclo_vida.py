"""Transiciones de estado del Documento."""

from __future__ import annotations

from typing import TYPE_CHECKING

from documento.entidad.constantes import (
    ESTADO_APROBADO_CLIENTE,
    ESTADO_APROBADO_EJECUTIVO,
    ESTADO_BORRADOR_CLIENTE,
    ESTADO_CON_ERRORES,
    ESTADO_EN_VALIDACION,
    ESTADO_NOTIFICADO_CLIENTE,
    ESTADO_PREAVISO_ENVIADO,
)

if TYPE_CHECKING:
    from documento.entidad.documento import Documento


def marcar_validacion(documento: Documento) -> None:
    documento.estado = ESTADO_EN_VALIDACION


def marcar_errores(documento: Documento, errores: list[str]) -> None:
    documento.errores_validacion = list(errores)
    documento.estado = ESTADO_CON_ERRORES


def aprobar_ejecutivo(documento: Documento) -> None:
    documento.errores_validacion.clear()
    documento.estado = ESTADO_APROBADO_EJECUTIVO


def marcar_preaviso(documento: Documento) -> None:
    documento.estado = ESTADO_PREAVISO_ENVIADO


def marcar_borrador_cliente(documento: Documento) -> None:
    documento.estado = ESTADO_BORRADOR_CLIENTE


def aprobar_cliente(documento: Documento) -> None:
    documento.estado = ESTADO_APROBADO_CLIENTE


def notificar_cliente(documento: Documento) -> None:
    documento.estado = ESTADO_NOTIFICADO_CLIENTE
