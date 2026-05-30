# Taller GOF — Documento (una sola clase de dominio)

Proceso logístico: cotización naviera → validación ejecutivo (digitado vs PDF) →
preaviso/borrador → aprobación cliente → novedades operativas.

Repositorio: [tallerGofDana](https://github.com/DanaSofia12/tallerGofDana.git)

## Estructura del proyecto

Dos capas claramente separadas bajo `documento/`:

```
documento/
├── entidad/                    # DOMINIO (solo Documento)
│   ├── documento.py          # Única clase de negocio
│   ├── constantes.py         # Estados y tipos (valores, no clases)
│   └── nucleo/               # Lógica por responsabilidad
│       ├── datos.py
│       ├── ciclo_vida.py
│       ├── novedades.py
│       └── consulta.py
│
└── patrones/                   # PATRONES GOF (sobre Documento)
    ├── builder/
    ├── factory_method/
    ├── singleton/
    ├── decorator/
    ├── strategy/
    ├── facade/
    └── command/
```

| Carpeta | Qué contiene |
|---------|----------------|
| **`entidad/`** | La clase `Documento` y su lógica interna. No hay otros patrones aquí. |
| **`patrones/`** | Los 7 patrones GOF; cada uno en su subcarpeta. Solo usan `Documento`. |

## Ejecución

```bash
python main.py
```

## Pruebas

Suite con `unittest` (stdlib), estructura paralela a `entidad/` y `patrones/`:

```bash
python -m unittest discover -s tests -v
```

Ver `documento/patrones/PATRONES.md` para el detalle por patrón.

## Importación

```python
from documento import Documento                    # entidad
from documento.patrones.facade import proceso      # patrón Facade
from documento.patrones.strategy import ejecutar_comparacion
```

## Patrones (carpeta `patrones/`)

| Subcarpeta | Rol |
|------------|-----|
| `builder/` | Construir `Documento` desde carpeta |
| `factory_method/` | Extraer PDF según naviera |
| `singleton/` | Canal único de notificaciones |
| `decorator/` | Vista en capas (auditoría, datos sensibles) |
| `strategy/` | Comparar MBL directo vs HBL consolidado |
| `facade/` | Flujo completo para el ejecutivo |
| `command/` | Aprobar, rechazar, notificar, novedad |
