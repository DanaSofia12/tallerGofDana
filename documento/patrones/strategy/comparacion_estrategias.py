"""Patrón Strategy: algoritmos de comparación digitado vs PDF."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from documento.entidad.constantes import CARGA_CONSOLIDADO, CARGA_DIRECTO, DOC_HBL_HIJO
from documento.entidad.documento import Documento


def _comparar_campo(
    nombre: str,
    digitado: dict[str, Any],
    pdf: dict[str, Any],
    errores: list[str],
) -> None:
    valor_d = digitado.get(nombre)
    valor_p = pdf.get(nombre)
    if valor_d is None and valor_p is None:
        return
    if str(valor_d).strip().lower() != str(valor_p).strip().lower():
        errores.append(
            f"Discrepancia en '{nombre}': digitado='{valor_d}' vs pdf='{valor_p}'"
        )


def comparar_mbl_directo(documento: Documento) -> list[str]:
    errores: list[str] = []
    digitado = _unificar_digitado(documento)
    pdf = _unificar_pdf(documento)
    for campo in documento.campos_comparables():
        _comparar_campo(campo, digitado, pdf, errores)
    return errores


def comparar_consolidado_hbl(documento: Documento) -> list[str]:
    errores: list[str] = []
    digitado = documento.datos_digitados
    pdf = documento.datos_pdf

    if documento.tipo_documento == DOC_HBL_HIJO:
        master_d = digitado.get("hbl_master")
        master_p = pdf.get("hbl_master")
        if master_d != master_p:
            errores.append(
                f"HBL hijo no coincide con master: {master_d} vs {master_p}"
            )

    hijos_d = digitado.get("hbl_hijos", [])
    hijos_p = pdf.get("hbl_hijos", [])
    if hijos_d and hijos_p and len(hijos_d) != len(hijos_p):
        errores.append(
            f"Cantidad HBL hijos distinta: {len(hijos_d)} vs {len(hijos_p)}"
        )

    for campo in documento.campos_comparables():
        _comparar_campo(campo, digitado, pdf, errores)
    return errores


def comparar_por_defecto(documento: Documento) -> list[str]:
    errores: list[str] = []
    for campo in documento.campos_comparables():
        _comparar_campo(
            campo, documento.datos_digitados, documento.datos_pdf, errores
        )
    return errores


def _unificar_digitado(documento: Documento) -> dict[str, Any]:
    base = {
        "numero_bl": documento.numero_bl,
        "shipper": documento.shipper,
        "consignee": documento.consignee,
        "puerto_origen": documento.puerto_origen,
        "puerto_destino": documento.puerto_destino,
        "fecha_salida": documento.fecha_salida,
        "fecha_llegada": documento.fecha_llegada,
        "nombre_barco": documento.nombre_barco,
        "viaje": documento.viaje,
    }
    base.update(documento.datos_digitados)
    return base


def _unificar_pdf(documento: Documento) -> dict[str, Any]:
    base = dict(_unificar_digitado(documento))
    base.update(documento.datos_pdf)
    return base


def resolver_estrategia(documento: Documento) -> Callable[[Documento], list[str]]:
    if documento.tipo_carga == CARGA_DIRECTO:
        return comparar_mbl_directo
    if documento.tipo_carga == CARGA_CONSOLIDADO:
        return comparar_consolidado_hbl
    return comparar_por_defecto


def ejecutar_comparacion(documento: Documento) -> list[str]:
    documento.marcar_en_validacion()
    estrategia = resolver_estrategia(documento)
    return estrategia(documento)
