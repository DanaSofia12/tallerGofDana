# Patrones GOF sobre `Documento`

Las pruebas automatizadas viven en `tests/` (no en scripts sueltos dentro de cada patrón).

## Ejecutar la suite

Desde la raíz del proyecto:

```bash
python -m unittest discover -s tests -v
```

## Estructura de pruebas

```
tests/
├── helpers.py              # Carga de fixtures (carpetas datos_ejemplo)
├── entidad/
│   └── test_documento.py   # Entidad pura
└── patrones/
    ├── test_builder.py
    ├── test_factory_method.py
    ├── test_singleton.py
    ├── test_decorator.py
    ├── test_strategy.py
    ├── test_command.py
    └── test_facade.py
```

Cada archivo de test valida el comportamiento del patrón homónimo en `documento/patrones/`.
