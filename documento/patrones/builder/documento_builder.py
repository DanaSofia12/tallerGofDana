"""Patrón Builder: construcción incremental de Documento (sin otra clase de dominio)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from documento.entidad.constantes import CARGA_DIRECTO, DOC_MBL, ESTADO_PDF_RECIBIDO
from documento.entidad.documento import Documento


def _estado_vacio() -> dict[str, Any]:
    return {
        "id_documento": "",
        "naviera": "",
        "tipo_carga": CARGA_DIRECTO,
        "tipo_documento": DOC_MBL,
        "numero_bl": "",
        "shipper": "",
        "consignee": "",
        "puerto_origen": "",
        "puerto_destino": "",
        "fecha_salida": "",
        "fecha_llegada": "",
        "nombre_barco": "",
        "viaje": "",
        "ruta_carpeta": "",
        "ruta_pdf": "",
        "datos_digitados": {},
        "datos_pdf": {},
    }


def iniciar() -> dict[str, Any]:
    return _estado_vacio()


def con_identificacion(
    estado: dict[str, Any],
    id_documento: str,
    naviera: str,
    tipo_carga: str,
    tipo_documento: str,
) -> dict[str, Any]:
    estado["id_documento"] = id_documento
    estado["naviera"] = naviera
    estado["tipo_carga"] = tipo_carga
    estado["tipo_documento"] = tipo_documento
    return estado


def con_bl(estado: dict[str, Any], numero_bl: str) -> dict[str, Any]:
    estado["numero_bl"] = numero_bl
    return estado


def con_partes(
    estado: dict[str, Any], shipper: str, consignee: str
) -> dict[str, Any]:
    estado["shipper"] = shipper
    estado["consignee"] = consignee
    return estado


def con_ruta(estado: dict[str, Any], origen: str, destino: str) -> dict[str, Any]:
    estado["puerto_origen"] = origen
    estado["puerto_destino"] = destino
    return estado


def con_fechas(estado: dict[str, Any], salida: str, llegada: str) -> dict[str, Any]:
    estado["fecha_salida"] = salida
    estado["fecha_llegada"] = llegada
    return estado


def con_transporte(estado: dict[str, Any], barco: str, viaje: str) -> dict[str, Any]:
    estado["nombre_barco"] = barco
    estado["viaje"] = viaje
    return estado


def desde_carpeta(estado: dict[str, Any], ruta_carpeta: str | Path) -> dict[str, Any]:
    carpeta = Path(ruta_carpeta)
    estado["ruta_carpeta"] = str(carpeta.resolve())
    meta = carpeta / "metadatos.json"
    if meta.exists():
        with meta.open(encoding="utf-8") as archivo:
            _aplicar_metadatos(estado, json.load(archivo))
    pdfs = list(carpeta.glob("*.pdf"))
    if pdfs:
        estado["ruta_pdf"] = str(pdfs[0].resolve())
    return estado


def _aplicar_metadatos(estado: dict[str, Any], datos: dict[str, Any]) -> None:
    for clave in (
        "id_documento",
        "naviera",
        "tipo_carga",
        "tipo_documento",
        "numero_bl",
        "shipper",
        "consignee",
        "puerto_origen",
        "puerto_destino",
        "fecha_salida",
        "fecha_llegada",
        "nombre_barco",
        "viaje",
    ):
        if clave in datos:
            estado[clave] = datos[clave]
    estado["datos_digitados"] = datos.get("datos_digitados", {})
    estado["datos_pdf"] = datos.get("datos_pdf", {})


def construir(estado: dict[str, Any]) -> Documento:
    return Documento(
        id_documento=estado["id_documento"] or "SIN-ID",
        naviera=estado["naviera"] or "DESCONOCIDA",
        tipo_carga=estado["tipo_carga"],
        tipo_documento=estado["tipo_documento"],
        numero_bl=estado["numero_bl"],
        shipper=estado["shipper"],
        consignee=estado["consignee"],
        puerto_origen=estado["puerto_origen"],
        puerto_destino=estado["puerto_destino"],
        fecha_salida=estado["fecha_salida"],
        fecha_llegada=estado["fecha_llegada"],
        nombre_barco=estado["nombre_barco"],
        viaje=estado["viaje"],
        ruta_carpeta=estado["ruta_carpeta"],
        ruta_pdf=estado["ruta_pdf"],
        estado=ESTADO_PDF_RECIBIDO,
        datos_digitados=dict(estado["datos_digitados"]),
        datos_pdf=dict(estado["datos_pdf"]),
    )
