"""Factory Method: selecciona función extractora según naviera del Documento."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from documento.entidad.documento import Documento
from documento.patrones.factory_method.extractores_naviera import EXTRACTORES


def extraer_desde_documento(documento: Documento) -> dict[str, Any]:
    clave = documento.naviera.strip().lower()
    extractor = EXTRACTORES.get(clave)
    if extractor is None:
        disponibles = ", ".join(sorted(EXTRACTORES))
        raise ValueError(
            f"Naviera '{documento.naviera}' sin extractor. Disponibles: {disponibles}"
        )
    if documento.ruta_pdf:
        return extractor(documento)
    carpeta = Path(documento.ruta_carpeta)
    datos = carpeta / "datos_pdf.json"
    if datos.exists():
        with datos.open(encoding="utf-8") as archivo:
            return json.load(archivo)
    return extractor(documento)
