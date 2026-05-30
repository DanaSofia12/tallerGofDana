"""Productos concretos del Factory Method: extracción por naviera."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

from documento.entidad.documento import Documento


def _leer_json(carpeta: Path, nombre: str) -> dict[str, Any]:
    ruta = carpeta / nombre
    if ruta.exists():
        with ruta.open(encoding="utf-8") as archivo:
            return json.load(archivo)
    return {}


def extraer_maersk(documento: Documento) -> dict[str, Any]:
    datos = _leer_json(Path(documento.ruta_carpeta), "formato_maersk.json")
    datos.setdefault("formato", "maersk")
    return datos


def extraer_msc(documento: Documento) -> dict[str, Any]:
    datos = _leer_json(Path(documento.ruta_carpeta), "formato_msc.json")
    datos.setdefault("formato", "msc")
    return datos


def extraer_cosco(documento: Documento) -> dict[str, Any]:
    datos = _leer_json(Path(documento.ruta_carpeta), "formato_cosco.json")
    datos.setdefault("formato", "cosco")
    return datos


EXTRACTORES: dict[str, Callable[[Documento], dict[str, Any]]] = {
    "maersk": extraer_maersk,
    "msc": extraer_msc,
    "cosco": extraer_cosco,
}
