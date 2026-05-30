"""Demostración usando únicamente la entidad Documento (sin patrones GOF)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from documento import Documento
from documento.entidad.constantes import ESTADO_PDF_RECIBIDO


def _leer_json(ruta: Path) -> dict[str, Any]:
    if not ruta.exists():
        return {}
    with ruta.open(encoding="utf-8") as archivo:
        return json.load(archivo)


def cargar_desde_carpeta(ruta_carpeta: str | Path) -> Documento:
    carpeta = Path(ruta_carpeta)
    meta = _leer_json(carpeta / "metadatos.json")
    pdfs = list(carpeta.glob("*.pdf"))

    documento = Documento(
        id_documento=meta.get("id_documento", "SIN-ID"),
        naviera=meta.get("naviera", "DESCONOCIDA"),
        tipo_carga=meta.get("tipo_carga", "directo"),
        tipo_documento=meta.get("tipo_documento", "mbl"),
        numero_bl=meta.get("numero_bl", ""),
        shipper=meta.get("shipper", ""),
        consignee=meta.get("consignee", ""),
        puerto_origen=meta.get("puerto_origen", ""),
        puerto_destino=meta.get("puerto_destino", ""),
        fecha_salida=meta.get("fecha_salida", ""),
        fecha_llegada=meta.get("fecha_llegada", ""),
        nombre_barco=meta.get("nombre_barco", ""),
        viaje=meta.get("viaje", ""),
        ruta_carpeta=str(carpeta.resolve()),
        ruta_pdf=str(pdfs[0].resolve()) if pdfs else "",
        estado=ESTADO_PDF_RECIBIDO,
        datos_digitados=meta.get("datos_digitados", {}),
        datos_pdf=meta.get("datos_pdf", {}),
    )

    naviera = documento.naviera.lower()
    datos_pdf = _leer_json(carpeta / f"formato_{naviera}.json")
    if datos_pdf:
        documento.registrar_datos_pdf(datos_pdf)
    if documento.datos_digitados:
        documento.registrar_datos_digitados(documento.datos_digitados)

    return documento


def ejecutar_demo(ruta_carpeta: str) -> None:
    documento = cargar_desde_carpeta(ruta_carpeta)

    print(f"\n=== Documento {documento.id_documento} ===")
    print(f"Naviera: {documento.naviera} | BL: {documento.numero_bl}")
    print(f"Tipo: {documento.tipo_documento} / {documento.tipo_carga}")
    print(f"Estado: {documento.estado}")

    vista = documento.vista_validacion()
    print("\n--- Vista validación (entidad) ---")
    print(f"Campos comparables: {documento.campos_comparables()}")
    print(f"Digitado vs PDF cargados: {bool(vista['digitado'])} / {bool(vista['pdf'])}")

    documento.marcar_en_validacion()
    print(f"Estado tras marcar validación: {documento.estado}")


if __name__ == "__main__":
    base = Path(__file__).parent / "datos_ejemplo"
    carpetas = [p for p in base.iterdir() if p.is_dir()]
    if not carpetas:
        print("No hay carpetas de ejemplo en datos_ejemplo/")
    for carpeta in carpetas:
        ejecutar_demo(str(carpeta))
